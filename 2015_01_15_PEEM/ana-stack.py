from pylab import *;
from pydao.io import Lox_Stack;
from pydao.ohdf import OGroup;
import gc;

# The procedure is:
# First load the images, which become array of integers. The maximum array element can be 2^24.
# The we normalize using preedge image. The results are stored in new img_array. The array elements are float, which are normally 1-2.
# Then we convert array to bmp by multiplying the array elements by 128. So we get values between 0 and 256.

isep = 1;

dirname = r'D:\CLS\2015_05_CLS_PEM\150513'
istack_cw = "150513001";
istack_ccw = "150513002";

disp_energy = 1507;
pre_energy = 1503;
post_energy = 1513;

#disp_energy = 710;
#pre_energy = 703;
#post_energy = 727;

#disp_energy = 1520;
#pre_energy = 1506;
#post_energy = 1570;

intnorm_method = "preedge";

roi0 = [100,400,100,500,];

# roi1 = [100,200,100,200];
# roi1 = [50,150,250,350];
# roi1 = [240,250,350,400,];

roi1 = [210,230,330,390];
roi2 = [350,420,100,180];

gc.collect();
lox = Lox_Stack(dirname,istack_cw);
lox.read_imgs(isep);
# lox=lox.select('Energy_eV_<545 and Energy_eV_>525');
lox.light_intensity_normalization(pre_energy,post_energy,method=intnorm_method);
# lox.linear_background_subtract(pre_energy,post_energy,method="preedge")
img_dbase_cw = lox;
gc.collect();

lox = Lox_Stack(dirname,istack_ccw);lox.read_imgs(isep);
# lox=lox.select('Energy_eV_<545 and Energy_eV_>525');
lox.light_intensity_normalization(pre_energy,post_energy,method=intnorm_method);
# lox.linear_background_subtract(pre_energy,post_energy,method="preedge")
img_dbase_ccw = lox;
# img_dbase_ccw.normalize(img_dbase_cw);
gc.collect();


######################################
figure(figsize=(16.0, 9.0));
# Energies = (array(img_dbase_cw.get_col('Energy_eV_'))+array(img_dbase_cw.get_col('Energy_eV_')))/2;
subplot(2,3,1);
img_dbase_cw.exe('_row.set("_dE",abs(Energy_eV_-disp_energy))',['disp_energy'],[disp_energy]);
minvalue,index = img_dbase_cw.min('_dE');
row_disp_cw = img_dbase_cw.get('rows')[index];
print "minvalue,index",minvalue,index
vmean = row_disp_cw.mean();
vstd = row_disp_cw.std();
vmin = vmean-2*vstd;
vmax = vmean+2*vstd;
row_disp_cw.disp_img(vmin=vmin,vmax=vmax);colorbar();
row_disp_cw.disp_roi(roi1);
row_disp_cw.disp_roi(roi2);


subplot(2,3,2);
img_dbase_ccw.exe('_row.set("_dE",abs(Energy_eV_-disp_energy))',['disp_energy'],[disp_energy]);
minvalue,index = img_dbase_ccw.min('_dE');
row_disp_ccw = img_dbase_ccw.get('rows')[index];
print "minvalue,index",minvalue,index
row_disp_ccw.disp_img(vmin=vmin,vmax=vmax);colorbar();
row_disp_ccw.disp_roi(roi1);
row_disp_ccw.disp_roi(roi2);

dif = row_disp_cw-row_disp_ccw;
subplot(2,3,3);
vstd = dif.std();
vmin = vmean-vstd;
vmax = vmean+vstd;
dif.disp_img(vmin=-1,vmax=1);colorbar();
dif.disp_roi(roi1);
dif.disp_roi(roi2);
dif.disp_roi(roi0);
title('Energy='+str(disp_energy));

subplot(2,3,4);
Energies,roi1_cw,roi1_ccw,dif_roi1 = img_dbase_cw.compare_roi(img_dbase_ccw,'Energy_eV_',roi=roi1);

subplot(2,3,5);
Energies,roi2_cw,roi2_ccw,dif_roi2 = img_dbase_cw.compare_roi(img_dbase_ccw,'Energy_eV_',roi=roi2);

subplot(2,3,6);
Energies,roi0_cw,roi0_ccw,dif_roi0 = img_dbase_cw.compare_roi(img_dbase_ccw,'Energy_eV_',roi=roi0);

show();

savetxt(istack_cw+'.txt',transpose(vstack((Energies,roi0_cw,roi0_ccw,dif_roi0,roi1_cw,roi1_ccw,dif_roi1,roi2_cw,roi2_ccw,dif_roi2))));
gcf().savefig(istack_cw+'.png');

savetxt(istack_cw+'_rois.txt',vstack((roi1,roi2)));
gcf().savefig(istack_cw+'.png');

img_dbase_cw.save_img();
img_dbase_ccw.save_img();

img_dbase_cw.save_diff(img_dbase_ccw);
