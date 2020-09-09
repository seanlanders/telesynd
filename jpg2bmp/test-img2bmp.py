from PIL import Image, ImageOps
import numpy as np
import glob
import binarize


bmpFiles = glob.glob('*.jpg')
for file in bmpFiles:
	print(file)
	prefix = file.split('.')
	prefix = prefix[0]
	target = prefix+"-binarize.bmp"
	target_path = binarize.binarize_image(prefix, file, target, 100)
	target_path= binarize.save_cpp(prefix, target_path)

"""
	img = Image.open(file)
	img.thumbnail((128,96))
	img = img.convert("1")
	inoBits = img.tobitmap(prefix)
	with open((prefix+"-test.cpp"), "wb") as binary_file:
		binary_file.write(inoBits)
		binary_file.close()
	img.save(prefix+"-test.bmp")
"""