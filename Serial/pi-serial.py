import serial
import serialweathertest as swt
from findArduino import findArduino
from credentials import credentials
import time

arduino = findArduino()
ser = serial.Serial(str(arduino), 9600)

def prepWeather(credential):
    weather = swt.weatherReport(credential)
    weatherMsg = ""
    counter = 0
    for key in weather.keys():
        if counter == 0:
            weatherMsg = str(weather[key])
            counter += 1
        else:
            weatherMsg = weatherMsg + ", " + str(weather[key])
    weatherMsg = weatherMsg + "\0"
    return weatherMsg

def decodeSerial(line, credential):
    print("Received: ", line)
    if b"1" in line:
        weather = prepWeather(credential)
        response = weather
    if b"2" in line:
        response = "Waiting . . . "
    else:
        print("Received: ", line)
        response = prepWeather(credential)
    return response

def encodeSerial(response):
    message = response.encode('utf-8')
    return message

def sendSerial(message, serialobj):
    try:
        serialobj.write(message)
        return True, (message.decode() + "message sent")
    except Exception as instance:
        return (False, instance)

if __name__ == '__main__':
#    weather = swt.weatherReport(credentials)
#    print(weather.keys())
    while 1:
        if(ser.in_waiting > 0):
            line = ser.readline()
            print(line)
            response = decodeSerial(line, credentials)
            message = encodeSerial(response)
            messageSent = sendSerial(message, ser)
            if messageSent[0] == True:
                print("Sent ",message)
            else:
                print(messageSent[1])
            time.sleep(60)
        


"""
# debug purposes only - may not work at all
        else:
            line = "weather".encode()
            response = decodeSerial((line), credentials)
            message = encodeSerial(response)
            messageSent = sendSerial(message, ser)
            if messageSent[0] == True:
                print("Sent ", message)
            else:
                print(messageSent[1])
            time.sleep(5)
"""