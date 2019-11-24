from PIL import Image
import os, sys

for infile in sys.argv[1:]:
	outfile = os.path.splitext(infile)[0]
	try:
		img = Image.open(sys.argv[1])
		data = img.getdata()
		img.mode = 'RGBA'

		r = [(d[0], d[0], d[0], 255) for d in data]
		g = [(d[1], d[1], d[1], 255) for d in data]
		b = [(d[2], d[2], d[2], 255) for d in data]
		a = [(d[3], d[3], d[3], 255) for d in data]

		img.putdata(r)
		img.save(outfile + '_R.png')
		img.putdata(g)
		img.save(outfile + '_G.png')
		img.putdata(b)
		img.save(outfile + '_B.png')
		img.putdata(a)
		img.save(outfile + '_A.png')
	except IOError:
		print("cannot Split '%s'")% infile