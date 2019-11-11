from PIL import Image
import os, sys

for infile in sys.argv[1:]:
	outfile = os.path.splitext(infile)[0] + "_Resize"
	try:
		img = Image.open(infile)
		
		New_size = (256, 256)
		larger_img = img.resize(New_size, Image.BICUBIC)
		larger_img.save(outfile + ".png", format="PNG")
	except IOError:
		print("cannot create icon for '%s'")% infile