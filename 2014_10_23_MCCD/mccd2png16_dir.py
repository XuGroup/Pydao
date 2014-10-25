from pylab import *;
from pydao.tools import mccd2png16, Progress_Teller;
import os;

dirname = r"C:\Home\360Cloud\WorkArchive\Field Work\2014_10_14DB\14-ID-B files";

files=os.listdir(dirname);
pt = Progress_Teller(len(files));

i=0;
for file in files:
	i=i+1;
	pt.tell(i);
	fullfile=os.path.join(dirname,file);
	print fullfile;
	if not os.path.isdir(fullfile):
		fs = file.split('.');
		if fs[-1]=='mccd':
			img_array = mccd2png16(fullfile);
			print "shape:",img_array.shape
		
