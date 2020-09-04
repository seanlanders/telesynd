from requests import get
import json
import os
import pytemperature
import credentials as credential

iconDir = os.getcwd() + "//icons"

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

def getlocdata(IP):
	locdataRequest = API["ipstack"]+IP+"?access_key=" + credential["ipstack"]
	print(locdataRequest)
	locdata = get(locdataRequest).text
	locdata = json.loads(locdata)
	return locdata

def getweather(loc):
	requestURL = API["openweather"] + "appid=" + credential["openweather"] + "&q=" + loc
	response = get(requestURL).text
	x = json.loads(response)
	return x

def downloadWeatherIcon(url, condition, dir):
	image_url = url
	save_name = dir + "//" + condition + ".png"
	urllib.request.urlretrieve(image_url, save_name)
	print("Downloaded %s, saved as %s" % (image_url, save_name))
	return save_name

def convertK2F(temperature):
	temp = pytemperature.k2f(temperature)
	return temp


ip = getIP()
print(ip)
locdata=getlocdata(ip)

print(len(locdata))

print(locdata.keys())
print(locdata['city'])
print(locdata['zip'])

location = locdata['city'] + ","+locdata['region_name']

weather = getweather(locdata['city'])
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

"""
from geolocation.main import GoogleMaps 
from geolocation.distance_matrix.client import DistanceMatrixApiClient

key = credential["google"]

google_maps = GoogleMaps(api_key=key)
location = google_maps.search(location="address")
print(location.all())
my_location=location.first()

print(my_location.city)
print(my_location.route)
print(my_location.street_number)
print(my_location.postal_code)
"""