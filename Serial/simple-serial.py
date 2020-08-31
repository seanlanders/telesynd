import serial
import serialweathertest as swt
from findArduino import findArduino
from credentials import credentials
import time

arduino = findArduino()
ser = serial.Serial(str(arduino), 9600)
ser.flush()

def prepWeather(credentials):
    weather = swt.weatherReport(credentials)
    weatherMsg = ""
    counter = 0
    for key in weather.keys():
        if counter == 0:
            weatherMsg = "\f" + key + ": " + str(weather[key])
            print(weatherMsg)
            counter += 1
        else:
            weatherMsg = weatherMsg + ", " + "\0" + key + ": " + str(weather[key])
            print(weatherMsg)
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
    counter = 0
    #sendSerial("Hello world".encode(), ser)
    #print("Sent hello world " + str(counter))
    time.sleep(5)
    while 1:

        #weatherMsg = prepWeather(credentials)
        #print(weatherMsg)
        #message = encodeSerial(weatherMsg)
        #messageSent = sendSerial(message, ser)
        #message = ("Hello world " + str(counter) + ("\n")).encode('utf-8')
        message = b'1'
        print(message)
        print(message.decode())
        messageSent = sendSerial(message, ser)
        if messageSent[0] == True:
            print("Sent ", message)
        else:
            print(messageSent[1])
        counter += 1
        time.sleep(10)