from pylab import *;
from enthought.mayavi import mlab;
from pylab import *;
from pydao.physics import Lattice,Atom;
from pydao.math import vcos,vXprod,mat_rotation_along,vlen,rotate_along;
from enthought.mayavi import mlab;

def find_alpha(theta, phi, theta1):
	alpha = arccos(sin(theta)*sin(phi)*sin(theta1)+cos(theta)*cos(theta1));
	return alpha;

def custom_thetaz(plane_normal,theta,phi):
    #thetaz is the angle between the incident x-ray and the z-axis,
    #theta is the diffraction angle
    thetazrange = arange(0,pi,pi/100000);
    r = plane_normal[0]*sin(thetazrange)*cos(phi)+plane_normal[1]*sin(thetazrange)*sin(phi)+plane_normal[2]*cos(thetazrange);
    f = abs(sin(theta)-r/((sin(thetazrange)*cos(phi))**2+(sin(thetazrange)*sin(phi))**2+cos(thetazrange)**2)**0.5/vlen(plane_normal));
    fmin = min(f);
    I = list(f).index(fmin);
    thetaz = thetazrange[I];
    return thetaz;

##########################################
phi = 90./180*pi; # the angle between the x-ray and the plane of normal of the surface and the diffraction plane
h,k,l=(1,0,6);

##########################################
# the x-ray
E = 12e3; # photon energy in eV
wavelength = 6.64e-34*3e8/E/1.6e-19*1e10; # wave length in angstrom
k_photon = 2*pi/wavelength;

#########################################
# the lattice and unit cell in real space
a=6.;
b=6.;
c=11.7;

a_axis=array([1.,0.,0.])*a;
b_axis=array([-0.5,sqrt(3)/2,0.])*b;
c_axis=array([0.,0.,1.])*c;

axis=array([a_axis,b_axis,c_axis]);
la=Lattice(basis=axis);
at=Atom();
at.set('position',zeros(3));
la.plot3d_basis(labelwidth = 0.01);
surfacenormal=array([0,0,1])

#########################################
# the k-space and diffraction plane
la.cal_kbasis();
kbasis=la.get('kbasis');

planenormal = h*kbasis[0]+k*kbasis[1]+l*kbasis[2];
theta = arcsin(vlen(planenormal)/k_photon/2);

##########################################
#angle between diffraction plane and surface
theta1 = arccos(vlen(planenormal*array([0,0,1]))/vlen(planenormal));
phi1 = arctan(planenormal[1]/planenormal[0]);

textwidth=0.005;

#######################
# the surface
x,y=mgrid[-100:101,-100:101]/100*a;
z=x-x;
mlab.mesh(x,y,z,opacity=0.5);
text='film surface'
mlab.text(1.1*a,0,'film surface',z=0,width=len(text)*textwidth)

at.plot3d(text='(0,0,0)');
mlab.quiver3d([0],[0],[0],[0],[0],[1],mode='2ddash',color=(0,0,1),scale_mode="none",scale_factor=6);
text='surface normal'
mlab.text(0,0,text,z=1.1*c,width=len(text)*textwidth)

##########################
# the diffraction plane
plane_kx=planenormal[0]/planenormal[2];
plane_ky=planenormal[1]/planenormal[2];

z=-plane_kx*x-plane_ky*y;
planenormal=planenormal/vlen(planenormal)*6;
mlab.mesh(x,y,z,opacity=0.5);

mlab.quiver3d([0], [0], [0],[planenormal[0]],[planenormal[1]],[planenormal[2]],color=(0,1,1),scale_mode="none",scale_factor=vlen(planenormal),mode='2ddash');
text='plane normal'+str((h,k,l))+'2theta='+str(2*theta/pi*180);
mlab.text(planenormal[0],planenormal[1],text,z=planenormal[2],width=len(text)*textwidth)

########################################
# the in-plane axis for the plane that represent intersection of the two planes
axis1=vXprod(surfacenormal,planenormal);axis1=axis1/vlen(axis1)*6;
text='axis1';
mlab.text(axis1[0],axis1[1],text,z=axis1[2],width=len(text)*textwidth);
axis2=vXprod(planenormal,axis1);axis2=axis2/vlen(axis2)*6;
text='axis2';
mlab.text(axis2[0],axis2[1],text,z=axis2[2],width=len(text)*textwidth);

mlab.quiver3d([0],[0],[0],[axis1[0]],[axis1[1]],[axis1[2]],scale_mode="none",scale_factor=vlen(axis1),mode='2darrow',color=(1,1,1));
mlab.quiver3d([0],[0],[0],[axis2[0]],[axis2[1]],[axis2[2]],scale_mode="none",scale_factor=vlen(axis2),mode='2darrow',color=(1,1,1));

######################################################################################
#the incident and diffracted beam with largest and lowest angles with the film surface
incident=rotate_along(axis1,pi/2-theta,planenormal);
incident=incident/vlen(incident)*6;
mlab.quiver3d([incident[0]],[incident[1]],[incident[2]],[-incident[0]],[-incident[1]],[-incident[2]],scale_mode="none",scale_factor=vlen(incident),mode='2darrow');
text='low incident'
mlab.text(incident[0],incident[1],text,z=incident[2],width=len(text)*textwidth)

incident=rotate_along(axis1,-pi/2+theta,planenormal);
incident=incident/vlen(incident)*6;
mlab.quiver3d([0], [0], [0],[incident[0]],[incident[1]],[incident[2]],scale_mode="none",scale_factor=vlen(incident),mode='2darrow');
text='low incident'
mlab.text(incident[0],incident[1],text,z=incident[2],width=len(text)*textwidth)
low_inc = incident;

#the incident and diffracted beam with medium angles with the film surface
incident=rotate_along(axis2,pi/2-theta,planenormal);
incident=incident/vlen(incident)*6;
mlab.quiver3d([incident[0]],[incident[1]],[incident[2]],[-incident[0]],[-incident[1]],[-incident[2]],scale_mode="none",scale_factor=vlen(incident),mode='2darrow');
text='medium incident';
mlab.text(incident[0],incident[1],text,z=incident[2],width=len(text)*textwidth)
med_inc = incident;

incident=rotate_along(axis2,-pi/2+theta,planenormal);
incident=incident/vlen(incident)*6;
mlab.quiver3d([0], [0], [0],[incident[0]],[incident[1]],[incident[2]],scale_mode="none",scale_factor=vlen(incident),mode='2darrow');
text='medium incident';
mlab.text(incident[0],incident[1],text,z=incident[2],width=len(text)*textwidth)

############################################################################
#the incident and diffracted beam with custom angles with the film surface
thetaz = custom_thetaz(planenormal,theta,phi); # the theta value in the lattice coordinate system

incident=rotate_along(array([0,1.,0]),thetaz,surfacenormal);
incident=rotate_along(surfacenormal,phi,incident);
# incident=rotate_along(planenormal,phi,incident);
incident=incident/vlen(incident)*6;
mlab.quiver3d([incident[0]],[incident[1]],[incident[2]],[-incident[0]],[-incident[1]],[-incident[2]],scale_mode="none",scale_factor=vlen(incident),mode='2darrow');
text='custom incident';
mlab.text(incident[0],incident[1],text,z=incident[2],width=len(text)*textwidth)
custom_inc = incident;

custom_axis = vXprod(incident,planenormal);
incident=rotate_along(custom_axis,pi-2*theta,incident);
incident=incident/vlen(incident)*6;
mlab.quiver3d([0], [0], [0],[incident[0]],[incident[1]],[incident[2]],scale_mode="none",scale_factor=vlen(incident),mode='2darrow');
text='custom incident';
mlab.text(incident[0],incident[1],text,z=incident[2],width=len(text)*textwidth)


mlab.show();
