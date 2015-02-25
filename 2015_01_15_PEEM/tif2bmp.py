from pylab import *;
from pydao.io import Lox_Stack,ImgArray;
from pydao.ohdf import OGroup;
import os;

dirname = r"D:\2014_12_CLSPEEM\141213";
filename = "141213016.tif";

tif_filename = os.path.join(dirname,filename);
img = ImgArray(tif_filename);
img.read();
#img.savebmp();

figure();
img_array = img.get('img_array');
imshow(img_array);
colorbar();
show();
