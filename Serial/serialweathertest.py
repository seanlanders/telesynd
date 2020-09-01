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

API={}
API["openweather"] = "http://api.openweathermap.org/data/2.5/weather?"
API["ipify"] = 'https://api.ipify.org/'
API["ipstack"] = 'http://api.ipstack.com/'

def getIP():
	ip = get(API["ipify"]).text
	return ip

def getLocdata(IP, credential):
	locdataRequest = API["ipstack"]+IP+"?access_key=" + credential["ipstack"]
	print(locdataRequest)
	locdata = get(locdataRequest).text
	locdata = json.loads(locdata)
	return locdata

def getWeather(loc, credential):
	requestURL = API["openweather"] + "appid=" + credential["openweather"] + "&q=" + loc
	response = get(requestURL).text
	weather = json.loads(response)
	return weather

def downloadWeatherIcon(url, condition, dir):
	image_url = url
	save_name = dir + "//" + condition + ".png"
	urllib.request.urlretrieve(image_url, save_name)
	print("Downloaded %s, saved as %s" % (image_url, save_name))
	return save_name

def convertK2F(temperature):
	temp = pytemperature.k2f(temperature)
	return temp

def weatherReport(fields, credential):
	ip = getIP()
	locdata = getLocdata(ip, credentials)
	location = locdata['city'] + ","+locdata['region_name']
	weather = getWeather(locdata['city'], credentials)
	if fields == "all":
		conditions = weather["weather"][0]["description"]
		shortconditions = weather["weather"][0]["main"]
		temperature = str(convertK2F(weather["main"]["temp"]))
		feelslike = str(convertK2F(weather["main"]["feels_like"]))
		humidity = str(weather["main"]["humidity"])
		results = {"temp": temperature, "feels": feelslike, "humidity": humidity, "longCond": conditions, "shortCond": shortconditions} 
	else:
		results = {}
		for x in range(len(fields)):
			if fields[x] == "conditions":
				conditions = weather["weather"][0]["description"]
				shortconditions = weather["weather"][0]["main"]
				results["conditions"] = conditions
				results["shortconditions"] = shortconditions
			elif fields[x] == "temperature":
				temperature = str(convertK2F(weather["main"]["temp"]))
				feelslike = str(convertK2F(weather["main"]["feels_like"]))
				results["temperature"] = temperature
				results["feelslike"] = feelslike
			elif fields[x] == "humidity":
				humidity = str(weather["main"]["humidity"])
				results["humdity"] = humidity
			else:
				print("ERROR-- only returning temp")
				temperature = str(convertK2F(weather["main"]["temp"]))
				results["temperature"] = temperature
				print(results["temperature"])
	print("Weather Report: ",results)
	return results

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
	weather = weatherReport(("all"), credentials)
	print("\n\n", weather)
	"""
	from geolocation.main import GoogleMaps 
	from geolocation.distance_matrix.client import DistanceMatrixApiClient

	key = "AIzaSyDW49kSJkSbUMIp0OVs7A8nNrE57iAecog"

	google_maps = GoogleMaps(api_key=key)
	location = google_maps.search(location="address")
	print(location.all())
	my_location=location.first()

	print(my_location.city)
	print(my_location.route)
	print(my_location.street_number)
	print(my_location.postal_code)
	"""
