from datetime import datetime, date
from pynytimes import NYTAPI
from credentials import key, secret
import json
import wayback
import time

nyt = NYTAPI(key)

today = date.today()
### intervals determine how far back into the NYT archive to reach
intervals = [150, 100,50,25,10,5,1]


### the basics of it - used to make a single request to NYT archives
### asks for articles on the given 'date'
def getArticles(date):
	articles = nyt.article_search(dates={"begin":datetime(date[0],date[1],date[2]), "end":datetime(date[0],date[1],date[2])})
	return articles

### iterates on getArticles across the intervals, 
### pulling N=peryear stories from each "articles" dump 
### 
def grabStories(dates, peryear):
	stories = {}
	year = []
	for date in dates:
		articles = getArticles(date)
		time.sleep(1)
		print("Grabbed ",date)
		for x in range(peryear):
			year.append(articles[x])	
		stories[date[0]] = year
	return stories

### SIMPLE / DETAILS 
### all "simple" functions get used in "details" as a simple way of 
### pulling relevant information from the json NYT returns
def simpleAbstract(article):
	try:
		abstract=article["abstract"].split('.')
		abstract = abstract[0] + '.'
	except:
		abstract = article["abstract"]
	return abstract

def simpleHeadline(article):
	headline = article["headline"]["main"]
	return headline

def simpleYear(article):
	maketime = datetime.strptime(article["pub_date"], "%Y-%m-%dT%H:%M:%S%z")	
	return maketime.year

def details(article):
	abstract = simpleAbstract(article)
	headline = simpleHeadline(article)
	year = simpleYear(article)
	return year, headline, abstract

### THIS SHOULD BE REPLACED WITH A FUNCTION THAT
### USES DETAILS TO PULL THE HEADLINE, ABSTRACT, YEAR
### + other relevant information
### AND THEN
### ANOTHER FUNCTION THAT FEEDS IT TO ARDUINO SERIALLY?
### ^- should actually probably get dropped into an ARDUINO package

def showStories(stories):
	for date in stories.keys():
		for x in range(len(stories[date])):
			year, headline, abstract = details(stories[date][x])
			print(year,"\n",headline,"\n",abstract)
		print("\n\n")

### To use this in NYT function:
### set today, intervals, peryear
###
### dates = wayback.goWayback(today,intervals)
### stories = grabStories(dates, peryear)
### develop some way of converting stories into data that can be
### communicated, serially, to arduino

if __name__ == '__main__':

	intervals=[150,100,50,10,1]
	peryear = 3

	dates = wayback.goWayback(today,intervals)
	print(dates)
	print("grabbing articles")
	year = []
	article = getArticles(dates[0])
	print("grabbed articles")
	print("grabbing ", peryear, " # of articles")
	stories = grabStories(dates, peryear)
	#showStories(stories)
	print(len(stories))
	print(stories.keys())
	for story in stories:
		print(stories[story])

"""	
	for x in range(peryear):
		year.append(article[x])
	stories = {}
	stories[dates[0][0]] = year

	print(len(stories[1870]))

	for date in stories.keys():
		for x in range(len(stories[date])):
			print(details(stories[date][x]))
"""

"""
	dates = wayback.goWayback(today, intervals)
	print(dates)
	print("grabbing stories")
	stories = grabStories(dates, peryear)
	print("Grabbed stories")
	print("showing stories")
	showStories(stories)
	print("showed stories")
"""

#print(article[0]["headline"]["main"], "\n", article[0]["abstract"])

"""
for date in dates:
	article = getArticles(dates[date])
	print(article[0]["headline"]["main"], article[0]["abstract"])
"""


#articles = nyt.article_search(dates={"begin":datetime.datetime(1920,8,27),"end":datetime.datetime(1920,8,27)})



#for article in articles:
#	print(article)