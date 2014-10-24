from pylab import *;

def findz_on_sphere(x,y,center,R):
	x0,y0,z0 = center;
	zz02 = R**2-(x-x0)**2-(y-y0)**2
	z1 = zz02**0.5+z0;
	z2 = z0-zz02**0.5;
	return z1,z2;

def findxz_on_screen(x,y,z,center,ke,d):
	x0,y0,z0 = center;
	theta = arcsin((z-z0)/ke);
	# rou = ((x-x0)**2+(y-y0)**2)**0.5;
	phi = arctan((x-x0)/(y-y0));
	# print "theta,phi",theta,phi
	y1 = d;
	x1 = tan(phi)*y1;
	z1 = (x1**2+y1**2)**0.5*tan(theta);
	return x1,z1;

##########################################
HV = 20e3; #the voltage of RHEED
alpha = 1.; #in degree, the incident angle
phi = 45; #in degree, the azimuthal angle 
pstyle = 'bo'; # b black, c cyan, g green, r red, k, black, m magenta, y yellow
N = 20; # maximum order to calculate
##########################################

a0 = 4e-10;   # lattice constant of STO in angstrom
ak0 = 2*pi/a0; # reciprocal space (k-space) lattice constant
	
ak = array([1,0,0])*ak0; # a-axis of the k-space
bk = array([0,1,0])*ak0; # b-axis of the k-space

me = 9.1e-31; # mass of electron
hbar =1.05e-34; # Plank constant
e_charge = 1.6e-19; # charge of an electron
Ee = HV*e_charge; # kinetic energy of electron
ke = (2*me*Ee)**0.5/hbar; # wave vector of the electron beam


y0 = ke*cos(alpha/180.*pi); #horizontal distance between the origin of the k-space and the center of the Ewald sphere.
z0 = 0.;
centerofsphere =  array([0.,y0,z0]); # Center of the Ewald sphere. We set the sample surface as z=0.

d_sample_screen = 1.; # distance between the sample and the screen

# N=20;
for h in range(-N,N+1): # (h,k) are the k-space indices
	for k in range(-N,N+1):
		g = ak*h+bk*k;
		xg0,yg0,zg = g;
		phi1=phi*pi/180;
		xg = xg0*cos(phi1)+yg0*sin(phi1); # rotate the k-space
		yg = -xg0*sin(phi1)+yg0*cos(phi1);
		z1,z = findz_on_sphere(xg,yg,centerofsphere,ke); # find the z on the Ewald sphere
		xs,zs = findxz_on_screen(xg,yg,z,centerofsphere,ke,d_sample_screen); # the x,z on the screen
		# print xg,z,xs,zs
		if isfinite(z):
			plot(xs,zs,pstyle);
			X = abs(h)+abs(k);
			if X<=3:
				text(xs,zs,'('+str(h)+','+str(k)+')',rotation=90);
	
# a few special points and lines on the screen
y = d_sample_screen*tan(alpha*pi/180);
plot(0,-y,'+r',ms=20); # this is the specular reflection (0,0).
text(0,-y,'Reflection',verticalalignment='top',horizontalalignment='center');
plot(0,y,'or',ms=20); # this is the transmission.
text(0,y,'Transmission',verticalalignment='top',horizontalalignment='center');

# make the x and y scale proportional
axis('tight');
xmin0,xmax0,ymin0,ymax0 = axis();
xrange = min(ymax0-ymin0,xmax0-xmin0)/1.5;
xmin = -xrange/2;
xmax = xrange/2;

ymax = ymax0; # xmax is kept to include the transmission
ymin =  ymax-xrange/4*3; 
axis([xmin,xmax,ymin,ymax]);

# zshade = d_sample_screen*sin(alpha/180.*pi);  # the boundary of the shadow of the substrate on the screen
# plot([xmin,xmax],[zshade,zshade]);
# axis([xmin,xmax,ymin,ymax]);
# print xrange,xmin,xmax,ymin,ymax;
show();
