from pylab import *;
from pydao.math import XyDiscreteFun;

data  = loadtxt(r'C:\Home\Dropbox\Programming\data_analysis\2014_11_10_find_spect_shift\S003_004_1.4mj_t2t+2.txt');

x = data[:,0];
y1 = data[:,1];
y2 = data[:,2];

sp1 = XyDiscreteFun();
sp1.set('x',x);
sp1.set('y',y1);
sp1.pick(xmin=50,xmax=130);

sp2 = XyDiscreteFun();
sp2.set('x',x);
sp2.set('y',y2);
sp2.pick(xmin=50,xmax=130);

subplot(1,2,1);
plot(x,y1)
plot(x,y2);

paras = sp1.find_xshift_renorm(sp2);
delta = paras[0];
factor = paras[1];
print paras;

x2fit = x+delta;
y2fit = y2*factor;

subplot(1,2,2);
plot(x,y1,'o-');
plot(x2fit,y2fit,'+-');

show();
