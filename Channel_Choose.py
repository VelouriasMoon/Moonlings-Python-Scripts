from PIL import Image
import numpy as np
import os, sys
import itertools as it

for infile in sys.argv[1:]:
	outfile = os.path.splitext(infile)[0]
	Rinput = int(sys.argv[2])
	Ginput = int(sys.argv[3])
	Binput = int(sys.argv[4])
	Ainput = int(sys.argv[5])
	
	try:
		img = Image.open(infile)
		data = img.getdata()
		img.mode = 'RGBA'
		width = img.width
		height = img.height
		rep = int(width*height)
		
		#for d in data:
		if Rinput <= 255:
			Rdata = it.repeat(int(sys.argv[2]), rep)
		else:
			Rdata = np.array(img.getdata(0))
			
		if Ginput <= 255:
			Gdata = it.repeat(int(sys.argv[3]), rep)
		else:
			Gdata = np.array(img.getdata(1))
			
		if Binput <= 255:
			Bdata = it.repeat(int(sys.argv[4]), rep)
		else:
			Bdata = np.array(img.getdata(2))
			
		if Ainput <= 255:
			Adata = it.repeat(int(sys.argv[5]), rep)
		else:
			Adata = np.array(img.getdata(3))
		
		img.putdata(list(zip(Rdata, Gdata, Bdata, Adata)))
		img.save(outfile + '_out.png', format="PNG")
	except IOError:
		pass