from PIL import Image
import os, sys

for infile in sys.argv[1:]:
	outfile = os.path.splitext(infile)[0]
	try:
		img = Image.open(infile)
		data = img.getdata()
		
		# Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
		rgb = [(d[0], d[1], d[2], 255) for d in data]
		a = [(d[3], d[3], d[3], 255) for d in data]

		img.mode = 'RGBA'
		img.putdata(rgb)
		img.save(outfile + '_RGB.png', format="PNG")
		img.putdata(a)
		img.save(outfile + '_A.png', format="PNG")
	except IOError:
		print("cannot Split '%s'")% infile