from pylab import *;
from pydao.tools import png162array;
import os;

dirname = r"C:\Home\360Cloud\WorkArchive\Field Work\2014_10_14DB\14-ID-B files";
filename = "S003_0.6mj_400ps2_060.png";

fullfile = os.path.join(dirname,filename);

img_array = png162array(fullfile);
imshow(img_array);colorbar();
show();

