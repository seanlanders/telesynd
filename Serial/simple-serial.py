import serial
import serialweathertest as swt
from findArduino import findArduino
from credentials import credentials
import time

arduino = findArduino()
ser = serial.Serial(str(arduino), 9600)

def prepWeather(credentials):
    weather = swt.weatherReport(credentials)
    weatherMsg = ""
    counter = 0
    for key in weather.keys():
        if counter == 0:
            weatherMsg = key + ": " + str(weather[key])
            counter += 1
        else:
            weatherMsg = weatherMsg + ", " + "\f" + key + ": " + str(weather[key])
    weatherMsg = "\0" + weatherMsg + "\0"
    return weatherMsg

def decodeSerial(line, credential):
    print("Received: ", line)
    response = "Recieved"
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
#   weather = swt.weatherReport(credentials)
#   print(weather.keys())
    time.sleep(5)
    sendSerial("Hello world".encode(), ser)
    print("Sent hello world")
    time.sleep(5)
    while 1:
        weatherMsg = prepWeather(credentials)
        #message = encodeSerial(weatherMsg)
        messageSent = sendSerial(weatherMsg, ser)
        if messageSent[0] == True:
            print("Sent ", message)
        else:
            print(messageSent[1])
        time.sleep(10)
