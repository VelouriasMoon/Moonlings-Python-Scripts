from PIL import Image
import numpy as np
import os, sys

for infile in sys.argv[2:]:
	outfile = os.path.splitext(infile)[0]
	choice = str(sys.argv[1])
	if choice == 'Split':
		img = Image.open(infile)
		data = img.getdata()
		
		rgb = [(d[0], d[1], d[2], 255) for d in data]
		a = [(d[3], d[3], d[3], 255) for d in data]

		img.mode = 'RGBA'
		img.putdata(rgb)
		img.save(outfile + '_RGB.png', format="PNG")
		img.putdata(a)
		img.save(outfile + '_A.png', format="PNG")
	elif choice == 'Merge':
		alphain = sys.argv[3]
		output = outfile.replace("_RGB", "")
		
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
	else:
		print('Unknown Choice')