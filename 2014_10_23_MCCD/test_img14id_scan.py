from pylab import *;
import pydao;
from pydao.io import Img14ID,Img14ID_AngleScan;
import os;

dirname = r"C:\Home\360Cloud\WorkArchive\Field Work\2014_10_14DB\14-ID-B files";
dirname = r'D:\Kishan\0.6mj_004_png16';

drol = 50;
drow = 50;
crow = 1718;
ccol = 3990;
roi = [1718-drow,1718+drow,3990-drol,3990+drol];

# load the scan, this will be a database automatically
scan = Img14ID_AngleScan(dirname,roi=roi);
scan.read_scan();

# select part of the scan
scan800ps = scan.select('pulsedelay==800');
iangles = scan800ps.get_col('iangle');
scan800ps.exe('_row.set("sum1",img_array.sum(1))',[],[]);
angle_vpix = scan800ps.get_col('sum1');
imshow(angle_vpix);
show();