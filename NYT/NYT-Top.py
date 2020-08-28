from pynytimes import NYTAPI
from credentials import key, secret
from PIL import Image, ImageOps
import numpy as np
import os, time

import urllib.request

identifierStrip = "https://nyti.ms/"
# Sets how many Top Stories to pull
storiesThreshold = 5

def makedir(dir):
	try:
		os.mkdir(dir)
		print("Made "+ dir)
	except:
		print(dir + " already exists!")
		pass

def makeIdentifier (identifierStrip, identifier):
	fileName = identifier.strip(identifierStrip)
	return fileName

def downloadImage(identifier, image, dir):
	image_url =  image
	save_name =  dir + "//" + identifier + ".jpg"
	urllib.request.urlretrieve(image_url, save_name)
	print("Downloaded %s, saved as %s" % (image_url, save_name))
	return save_name

def saveMetadata(identifier, entry, dir):
	# make sure to write the news story's metadata to a filename
	values = entry
	fileName = dir + "//" + makeIdentifier(identifierStrip, identifier) + ".txt"
	f = open(fileName, "w")
	f.write(str(values))
	print("Saved to %s" % (fileName))
	return fileName

def jpg2bmp(identifier, image, dir):
	img = Image.open(image)
	ary = np.array(img)

	#split the three channels
	r,g,b = np.split(ary,3,axis=2)
	r=r.reshape(-1)
	g=r.reshape(-1)
	b=r.reshape(-1)

	#RGB to grayscale
	bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2],zip(r,g,b)))
	bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
	bitmap = np.dot((bitmap > 128).astype(float),255)
	im = Image.fromarray(bitmap.astype(np.uint8))
	tempFile = dir + "//" + identifier + "-temp.bmp"
	im.save(tempFile)
	print("Saved " + tempFile)
#	return tempFile
# this is broken - "not a bitmap" error
	inoSave = dir + "//" + identifier + ".cpp"
	im2 = Image.open(tempFile)
	im2 = im2.convert(mode="1")
	inoBits = im2.tobitmap(identifier)
#	np.savetxt(inoSave, array, fmd="%d")
	with open(inoSave, "wb") as binary_file:
		binary_file.write(inoBits)
		binary_file.close()
	return tempFile, inoSave 


tempDir = os.getcwd() + "//temp"
thumbsTemp = tempDir + "//thumbs"
bmpsTemp = tempDir + "//bmps"
txtsTemp = tempDir + "//text"

makedir(tempDir)
makedir(thumbsTemp)
makedir(bmpsTemp)
makedir(txtsTemp)

print(tempDir,thumbsTemp,bmpsTemp)

#print(key, secret)

nyt=NYTAPI(key)

top_stories = nyt.top_stories()

with open("stories-keys.txt", "w") as f:
	f.write(str(top_stories[0].keys()))
	f.close()
with open("multimedia-keys.txt", "w") as f:
	f.write(str(top_stories[0]["multimedia"][0].keys()))
	f.close()

stories = []
downloadedImage = []
savedMetadata = []
savedTitle = []

for x in range(len(top_stories)):
	tempStory = top_stories[x]
#	print(top_stories[x]["title"],)
	for y in range(len(tempStory["multimedia"])):
		try:
			tempMultimedia = tempStory["multimedia"][y]
			if tempMultimedia["format"] == "Standard Thumbnail":
				print(tempStory["short_url"])
				identifier = makeIdentifier(identifierStrip, tempStory["short_url"])
				print(identifier)
				downloadedImage.append(downloadImage(identifier, tempMultimedia["url"], thumbsTemp))
				savedMetadata.append(saveMetadata(identifier, tempStory, txtsTemp))
				savedTitle.append(tempStory["title"])
				savedStory = {"title":savedTitle[x], "metadata":savedMetadata[x],"image":downloadedImage[x],"identifier":identifier}
				stories.append(savedStory)
				time.sleep(1)
		except:
			print("no multimedia")
			pass
		#print("\t", top_stories[x]["multimedia"][y]["url"], top_stories[x]["multimedia"][y]["format"])
	#stories.append(tempStory["title"])

counter = 0
storiesLen = len(stories)
currentStory = (storiesLen-1) - counter
inoEntries = []

while counter < storiesThreshold:
	#try:
	identifier = stories[currentStory]["identifier"]
	print(identifier)
	try:
		savedBMP,savedCPP = jpg2bmp(identifier, stories[currentStory]["image"], bmpsTemp)
		inoEntries.append({"image":savedBMP,"title":stories[currentStory]["title"]})
		counter += 1

	except:
		print("image save didn't work")
		pass
#	savedBMP = jpg2bmp(identifier, stories[currentStory]["image"], bmpsTemp)
	
	#except:
	#	pass
	currentStory = currentStory - 1
	print(currentStory)
print(inoEntries)
print(len(inoEntries))
