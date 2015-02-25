from pylab import *;
from pydao.io import Lox_Stack,ImgArray;
from pydao.ohdf import OGroup;
import os;

dirname = r"D:\2014_12_CLSPEEM\141212";

files = os.listdir(dirname);

for file in files:
	if file.endswith('.tif'):
		tif_filename = os.path.join(dirname,file);
		img = ImgArray(tif_filename);
		img.read(dtype=0);
		img.savebmp(renormalize='minmax');
