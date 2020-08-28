from PIL import Image, ImageOps
import numpy as np

img = Image.open('AlanTuring.jpg')
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
im.thumbnail((128,96))
inverted_image = ImageOps.invert(im)
im.save('AlanTuring.bmp')
inverted_image.save('AlanTuring-inverted.bmp')
im2 = Image.fromarray(bitmap.astype(np.uint8))
im2 = im2.convert(mode="1")
ary2 = np.array(im2)
print(ary2)
im2.thumbnail((128,96))
im2.save("mode1.bmp")


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