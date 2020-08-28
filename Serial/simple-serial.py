import serial
import serialweathertest as swt
from findArduino import findArduino
from credentials import credentials
import time

arduino = findArduino()
ser = serial.Serial(str(arduino), 9600)

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
            time.sleep(5000)
        sendSerial("Hello world".encode(), ser)