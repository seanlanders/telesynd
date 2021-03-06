from requests import get
import json
import os
import pytemperature
from credentials import credentials

iconDir = os.getcwd() + "//icons"

# Make directory to store icons in 
# MAYBE OFFLOAD INTO THE GRAPHICS HANDLER THAT DOES JPG2BMP?
# def newrequest(type, dir):
#	newDir = os.getcwd() + "//" + type
#	try:
#		os.mkdir(newDir)
#		print("Created ", newDir, " for ", type)
#	except Exception as instance:
#		print("Couldn't make ", newDir, " because ", instance) 
try:
	os.mkdir(iconDir)
	print("Created " + iconDir)
except:
	print("Already had dir " + iconDir)

# just in case API changes
# consider externalizing + importing
API={}
API["openweather"] = "http://api.openweathermap.org/data/2.5/weather?"
API["ipify"] = 'https://api.ipify.org/'
API["ipstack"] = 'http://api.ipstack.com/'

# get user's external IP
def getIP():
	ip = get(API["ipify"]).text
	return ip

#using user's IP, get best guess of user's location 
def getLocdata(IP, credential):
	locdataRequest = API["ipstack"]+IP+"?access_key=" + credential["ipstack"]
	print(locdataRequest)
	locdata = get(locdataRequest).text
	locdata = json.loads(locdata)
	return locdata

# using best guess of user's location, get prevailing weather conditions from openweather 
def getWeather(loc, credential):
	requestURL = API["openweather"] + "appid=" + credential["openweather"] + "&q=" + loc
	response = get(requestURL).text
	weather = json.loads(response)
	return weather

# to download the current Weather Icon
# TODO: convert icon to 1-bit BMP, and communicate to Arduino (serially?)
def downloadWeatherIcon(url, condition, dir):
	image_url = url
	save_name = dir + "//" + condition + ".png"
	urllib.request.urlretrieve(image_url, save_name)
	print("Downloaded %s, saved as %s" % (image_url, save_name))
	return save_name

# right now, openweather replies back in Kelvin
# this function translates to F
def convertK2F(temperature):
	temp = pytemperature.k2f(temperature)
	return temp

# how we get the weather
# if/else tree really needs some finessing
def weatherReport(fields, credential):
	ip = getIP()
	locdata = getLocdata(ip, credentials)
	location = locdata['city'] + ","+locdata['region_name']
	weather = getWeather(locdata['city'], credentials)
	if "all" in fields:
		conditions = weather["weather"][0]["description"]
		shortconditions = weather["weather"][0]["main"]
		temperature = str(convertK2F(weather["main"]["temp"]))
		feelslike = str(convertK2F(weather["main"]["feels_like"]))
		humidity = str(weather["main"]["humidity"])
		results = {"temp": temperature, "feels": feelslike, "humid": humidity, "longCond": conditions, "shortCond": shortconditions} 
	else:
		results = {}
		for x in range(len(fields)):
			print(fields[x])
			if fields[x] == "conditions":
				conditions = weather["weather"][0]["description"]
				shortconditions = weather["weather"][0]["main"]
				results["longCond"] = conditions
				results["shortCond"] = shortconditions
			elif fields[x] == "temperature":
				temperature = str(convertK2F(weather["main"]["temp"]))
				feelslike = str(convertK2F(weather["main"]["feels_like"]))
				results["temp"] = temperature
				results["feels"] = feelslike
			elif fields[x] == "humidity":
				humidity = str(weather["main"]["humidity"])
				results["humd"] = humidity
			else:
				print("ERROR-- only returning temp")
				temperature = str(convertK2F(weather["main"]["temp"]))
				results["temperature"] = temperature
				print(results["temperature"])
	print("Weather Report: ",results)
	return results

# used for debugging / example
if __name__ == '__main__':

	ip = getIP()
	print(ip)
	locdata=getLocdata(ip, credentials)

	print(len(locdata))

	print(locdata.keys())
	print(locdata['city'])
	print(locdata['zip'])

	location = locdata['city'] + ","+locdata['region_name']

	weather = getWeather(locdata['city'], credentials)
	print(weather.keys())
	for key in weather.keys():
		print(key + ": " + str(weather[key]))

	#weatherIcon = downloadWeatherIcon(weather["weather"]["icon"], weather["weather"]["main"], iconDir)
	#print(weatherIcon)

	print("\n\n")
	print("Weather in " + location)
	print("Conditions: " + str(weather["weather"][0]["description"]))
	print("Temperature: " + str(convertK2F(weather["main"]["temp"])) + "F, (feels like " + str(convertK2F(weather["main"]["feels_like"])) + "F)")
	print("Humidity: " + str(weather["main"]["humidity"]) + "%")

	weather = weatherReport(("temperature", "humidity"), credentials)
	print("\n\n", weather)
	print(weather["temp"])
	weather = weatherReport(("all"), credentials)
	print("\n\n", weather)
	"""
	from geolocation.main import GoogleMaps 
	from geolocation.distance_matrix.client import DistanceMatrixApiClient

	# insert your own API credentials
	key = credentials["google"]

	google_maps = GoogleMaps(api_key=key)
	location = google_maps.search(location="address")
	print(location.all())
	my_location=location.first()

	print(my_location.city)
	print(my_location.route)
	print(my_location.street_number)
	print(my_location.postal_code)
	"""
