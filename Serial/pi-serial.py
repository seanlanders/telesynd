import serial
import serialweathertest as swt
from findArduino import findArduino
from credentials import credentials

arduino = findArduino()
ser = serial.Serial(str(arduino), 9600)

def decodeSerial(line):
	if line == "weather":
		weather = swt.weatherReport()
		for key in weather.keys():
			weatherMsg = weatherMsg + str(weather["key"])
		print(weatherMsg)
		ser.write(weatherMsg)
	return response

def encodeSerial(response):
	message = response.encode()
	return message

def sendSerial(message, serialobj):
	try:
		serialobj.write(message)
		return True, (message.decode() + "message sent")
	except Exception as instance:
		return (False, instance)

if __name__ == '__main__':
	weather = swt.weatherReport()
	print(weather.keys())


"""
	while 1: 
	    if(ser.in_waiting > 0):
	        line = ser.readline()
	        print(line)
	        response = decodeSerial(line)
	        message = encodeSerial(response)
	        messageSent = sendSerial(message)
	       	if messageSent[0] == True:
	       		pass
	       	else:
	    		print(messageSent[1])
"""