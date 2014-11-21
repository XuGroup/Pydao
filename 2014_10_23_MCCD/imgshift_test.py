from pylab import *;
from pydao.io import ImgArray;

file0 = r'C:\Home\Dropbox\Programming\data_analysis\2014_11_20_2Dimageshift\S003_1mj_-2ns1_106L_0.txt';
file1 = r'C:\Home\Dropbox\Programming\data_analysis\2014_11_20_2Dimageshift\S003_1mj_100ps1_106L_0.txt';

#file0 = r'C:\Home\Dropbox\Programming\data_analysis\2014_11_20_2Dimageshift\S003_1mj_-2ns1_106L_1.txt';
#file1 = r'C:\Home\Dropbox\Programming\data_analysis\2014_11_20_2Dimageshift\S003_1mj_100ps1_106L_1.txt';

##############################################
## load the data
##############################################
data0 = loadtxt(file0);
data1 = loadtxt(file1);
data0 = data0-data0.min();
data1 = data1-data1.min();

print data0.shape
print data1.shape

#data0 = data0[:,100:320];
data0 = data0[:,200:400];

#############################################
## process of the images
#############################################
img0= ImgArray(); img0.set('img_array',data0);
img1= ImgArray(); img1.set('img_array',data1);

nslope = 2;
img0.remove_spikes(nslope=nslope);
img1.remove_spikes(nslope=nslope);

new_mimg,paras = img0.find_match(img1,paras0=None);

#############################################
## plot the images
#######################################
data0 = img0.get('img_array');
data1 = img1.get('img_array');

subplot(2,3,1);
imshow(data0);colorbar();

subplot(2,3,2);
imshow(data1);colorbar();

subplot(2,3,3);
datadiff=data1-data0;
imshow(datadiff,vmin=datadiff.mean()-3*datadiff.std(),vmax=datadiff.mean()+3*datadiff.std());colorbar()
data2 = new_mimg.get('img_array');

subplot(2,3,6);
datadiff2=data1-data2;
imshow(datadiff2,vmin=datadiff2.mean()-3*datadiff2.std(),vmax=datadiff2.mean()+3*datadiff2.std());colorbar();
show();
#############################################
## plot the integration
#######################################

subplot(2,3,4);
plot(data0.sum(0),'+');
plot(data1.sum(0),'o');
plot(data2.sum(0));
xlabel('column');

subplot(2,3,5);
plot(data0.sum(1),'+');
plot(data1.sum(1),'o');
plot(data2.sum(1));
xlabel('row');

#####################################################
# linear shift fit (consider factor and background)
#####################################################
from pydao.math import XyDiscreteFun;
#print img0.nthmoment(1);
#print img1.nthmoment(1);
#print new_mimg.nthmoment(1);


N,M = data0.shape;
x = arange(M);
y0 = data0.sum(0);
y1 = data1.sum(0);

sp0 = XyDiscreteFun();
sp0.set('x',x);
sp0.set('y',y0);
sp1 = XyDiscreteFun(x);
sp1.set('x',x);
sp1.set('y',y1);

paras = sp1.find_xshift_renormbg(sp0);
delta = paras[0];
factor = paras[1];
bg = paras[2];
print "shift in columns",paras;
x1fit = x+delta;
y1fit = y0*factor+bg;
subplot(2,3,4);
plot(x1fit,y1fit,linewidth=4);


x = arange(N);
y0 = data0.sum(1);
y1 = data1.sum(1);

sp1 = XyDiscreteFun(x);
sp1.set('x',x);
sp1.set('y',y1);
sp0 = XyDiscreteFun();
sp0.set('x',x);
sp0.set('y',y0);

paras = sp1.find_xshift_renormbg(sp0);
delta = paras[0];
factor = paras[1];
bg = paras[2];
print "shift in rows:",paras;
x1fit = x+delta;
y1fit = y0*factor+bg;
subplot(2,3,5);
plot(x1fit,y1fit,linewidth=4);

show()
