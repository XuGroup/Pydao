from pylab import *;
from pydao.io import Lox_Stack,ImgArray;
from pydao.ohdf import OGroup;
import os;

dirname = r"E:\2014_08_CLS\140801\140801020";
filename_pre = "140801020#1.tif"; 
filename = "140801020#107.tif"; 

tif_filename_pre = os.path.join(dirname,filename_pre);
img_pre = ImgArray(tif_filename_pre);

tif_filename = os.path.join(dirname,filename);
img = ImgArray(tif_filename);

img_array_pre = img_pre.get('img_array');
img_array = img.get('img_array');

subplot(2,2,1);
imshow(img_array_pre);
colorbar();

subplot(2,2,2);
imshow(img_array);
colorbar();

subplot(2,2,3);
imshow(img_array/img_array_pre);
colorbar();

show();