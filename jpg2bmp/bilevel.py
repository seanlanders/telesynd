from PIL import Image
import glob

bmpFiles = glob.glob('*.jpg')
for file in bmpFiles:
	print(file)
	prefix = file.split('.')
	prefix = prefix[0]
	target = prefix+"-bilevel.bmp"
	img = Image.open(file)
	thresh = 200
	fn = lambda x : 255 if x > thresh else 0
	r = img.convert('L').point(fn, mode='1')
	r.thumbnail((128,96))
	r.save(target)
	inoBits = r.tobitmap(prefix)
	with open((prefix+"-bilevel.cpp"), "wb") as binary_file:
		binary_file.write(inoBits)
		binary_file.close()
	img.save(prefix+"-bilevel.bmp")