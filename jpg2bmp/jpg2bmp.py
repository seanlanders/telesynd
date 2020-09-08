from PIL import Image, ImageOps
import numpy as np
import glob

bmpFiles = glob.glob('*.jpg')
for file in bmpFiles:
	print(file)
	prefix = file.split('.')
	prefix = prefix[0]
	img = Image.open(file)
	ary = np.array(img)

	# Split the three channels
	r,g,b = np.split(ary,3,axis=2)
	r=r.reshape(-1)
	g=r.reshape(-1)
	b=r.reshape(-1)

	# Standard RGB to grayscale 
	bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], 
	zip(r,g,b)))
	bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
	bitmap = np.dot((bitmap > 128).astype(float),255)
	im = Image.fromarray(bitmap.astype(np.uint8))
	inverted_image = ImageOps.invert(im)
	im.save((prefix+".bmp"))

	inverted_image.save((prefix + "inverted-.bmp"))
	im2 = Image.fromarray(bitmap.astype(np.uint8), mode="L").convert("1")
	im2.thumbnail((128,96))
	inoBits = im2.tobitmap(prefix)
	im2.save((prefix+"-resized.bmp"))
	with open((prefix+".cpp"), "wb") as binary_file:
		binary_file.write(inoBits)
		binary_file.close()
"""
ary2 = np.array(im2)
print(ary2)
im2.thumbnail((128,96))
im2.save("mode1.bmp")
"""
"""
i = Image.open("AlanTuring.bmp")

inoBits = i.convert(mode="1")
inoBits = inoBits.tobitmap("AlanTuring")
print(inoBits)
#remade = Image.frombytes(mode="1", size=(128,96), inoBits)
#remade.save("nicetry.bmp")

print(type(inoBits))
with open("AlanTuring.cpp", "wb") as binary_file:
	binary_file.write(inoBits)
	binary_file.close()

i = Image.open("mode1.bmp")
i = i.convert(mode="L")
i = i.convert(mode="1")
inoBits = i.tobitmap("mode1")
	
with open("mode1.cpp", "wb") as binary_file:
	binary_file.write(inoBits)
	binary_file.close()
	"""