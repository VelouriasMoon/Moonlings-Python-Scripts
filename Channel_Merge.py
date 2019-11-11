import numpy as np
from PIL import Image
import os, sys

for infile in sys.argv[1:]:
	alphain = sys.argv[2]
	outfile = os.path.splitext(infile)[0]
	output = outfile.replace("_RGB", "")
	try:
		img = Image.open(infile)
		data = img.getdata()
		alpha = Image.open(alphain)
		adata = np.array(alpha.getdata(0))

		r = np.array(img.getdata(0))
		g = np.array(img.getdata(1))
		b = np.array(img.getdata(2))

		img.mode = 'RGBA'
		img.putdata(list(zip(r, g, b, adata)))
		img.save(output + '.png', format="PNG")
	except IOError:
		pass