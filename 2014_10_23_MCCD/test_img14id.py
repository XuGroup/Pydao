from pylab import *;
import pydao;
from pydao.io import Img14ID,Img14ID_AngleScan;
import os;

dirname = r"C:\Home\360Cloud\WorkArchive\Field Work\2014_10_14DB\14-ID-B files";
# dirname = r'D:\Kishan\0.6mj_004_png16';

# filename = "S003_0.6mj_400ps2_060.png";
filename = r'S003_0.6mj_1.6ns1_094.png';

fullfile = os.path.join(dirname,filename);
print "fullfile:",fullfile

wrol = 100;
wrow = 200;
roi = [1718-wrow,1718+wrow,3990-wrol,3990+wrol];

img = Img14ID(fullfile);
img.read(roi=roi);
img.disp();
show();

print "sample_name:",img.get('sample_name')
print "fluence:",img.get('fluence')
print "pulsedelay:",img.get('pulsedelay')
print "pulsedelayunit:",img.get('pulsedelayunit');
print "iscan:",img.get('iscan');
print "iangle:",img.get('iangle');