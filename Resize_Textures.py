from PIL import Image
import os, sys

for infile in sys.argv[1:]:
	New_Hight = int(sys.argv[2])
	New_Width = int(sys.argv[3])
	imgFormat = int(sys.argv[4])
	outfile = os.path.splitext(infile)[0]
	try:
		img = Image.open(infile)
		
		New_size = (New_Hight, New_Width)
		print("Thonking")
		larger_img = img.resize(New_size, imgFormat)
		larger_img.save(outfile + ".png", format="PNG")
		print("Done")
	except IOError:
		pass