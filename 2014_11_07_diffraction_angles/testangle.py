from pylab import *;
from pydao.physics import Wave,CystalDiffraction,CrystalPlane,Lattice;

############################
# Here is pretty much all the inputs
phic = 210/180.*pi;
index = (1,0,6);
photoenergy = 12e3*1.6e-19

##########################################
## First we setup the diffraction plane
a=6.;
b=6.;
c=11.7;
la = Lattice();
basis=la.length_angle_2basis([a,b,c],[90.,90.,120.]);
la.set('basis',basis);
plane = CrystalPlane(lattice=la,index=index);
plane.plot();

###########################################
# Then the energy of the diffraction wave
wave = Wave(type='EM',energy = photoenergy);

###########################################
# Align the diffraction plane and the wave using the assigned phic or thetac
dif = CystalDiffraction(plane = plane, incidentwave = wave);
theta = dif.cal_theta();
print "2theta:",theta*2*180/pi;

incident = dif.align_incident(phic = phic);
thetac, phic = (incident.reverse()).get_angles(); # Here the convension is that the angle is calculated from the vector that is the inverse of the incident.
print "aligned, found thetac,phic:",thetac*180/pi,phic*180/pi,'degree'

incident.plot(text='incident',textposition ='start', resizemethod = 'fixend',factor=6);

diffracted = dif.find_diffracted();
diffracted.plot(text='diffracted',textposition ='end' ,resizemethod = 'fixstart',factor=6);

#####################################################################
# Additionl calculation to see what the range of thetac and phic are
rotationrange,thetacs,phics = dif.angle_range();
print "thetac range:",array([min(thetacs),max(thetacs)])*180/pi,'degree';
print "phic range:",array([min(phics),max(phics)])*180/pi,'degree';

subplot(1,2,1);
plot(rotationrange/pi*180,thetacs/pi*180,'o');
plot(rotationrange/pi*180,phics/pi*180,'o');
xlabel('Cone Angle (degree)');
ylabel('Angles in Lattice Coordinate System (degree)');
legend(['thetac','phic']);
grid(True);
axis('tight');
subplot(1,2,2);
plot(phics/pi*180,thetacs/pi*180,'o-');
xlabel('phic (degree)');
ylabel('thetac (degree)');
plot(phic/pi*180,thetac/pi*180,'p');
text(phic/pi*180,thetac/pi*180,'current position');
grid(True);
axis('tight');
show();
