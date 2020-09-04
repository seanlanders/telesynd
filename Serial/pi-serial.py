import serial
#TODO rename from clearly temp 'test' name
import serialweathertest as swt
from findArduino import findArduino
from credentials import credentials
import time

# might be good to store baud externally in config file
# common reference for Pi + Arduino
baud = 57600
arduino = findArduino()
ser = serial.Serial(str(arduino), baud)

# draws on swt weatherReport to retrieve weather conditions
# possible fields, at present:
# 'all' returns conditions, shortconditions, temperature, feelslike, humidity 
# 'conditions' - returns 'conditions' and 'shortconditions', which describe weather in plaintext
# 'temperature' - returns temp and feelslike in F
## TODO add flag for F or C - controlled by external toggle?
# 'humidity' - returns humidity %
# all values returned as dictionary, each entry as string
def prepWeather(fields, credential):
    weather = swt.weatherReport((fields), credential)
    weatherMsg = ""
    counter = 0
    for key in weather.keys():
        print(key,)
        if counter == 0:
            weatherMsg = str(weather[key])
            counter += 1
        else:
            weatherMsg = weatherMsg + ", " + str(weather[key])
    weatherMsg = "<" + weatherMsg + ">"
    return weatherMsg

# responds to code from Arduino 
# numeric code determines what should be returned
# TODO build out
# this + next three should probably get externalized and imported
def decodeSerial(line, credential):
    print("Received: ", line)
    if b"1" in line:
        weather = prepWeather(("temperature", "humidity"), credential)
        response = weather
    elif b"2" in line:
        response = "Waiting . . . "
    elif b"weather" in line:
        response = prepWeather(("temperature"), credential)
        print("WEATHER!")
    else:
        print("Received: ", line)
        response = "NOPE"
    print(response)
    return response

# encodes response for sending to Arduino
# may need to be more complex & include formatting
def encodeSerial(response):
    message = response.encode('utf-8')
    return message

# sends bytes to Arduino; reports the results
# returns a boolean value, and message that was sent (+ error if not sent)
def sendSerial(message, serialobj):
    try:
        serialobj.write(message)
        return True, (message.decode() + "message sent")
    except Exception as instance:
        return (False, instance)

if __name__ == '__main__':
    # Debug code to make sure weather report works
    #weather = swt.weatherReport(("temperature"), credentials)
    #print(weather.keys())
    #print(weather[0])
    #print(weather["temperature"])
    #
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
        # debug purposes only - may not work at all
        else:
            line = "weather".encode()
            response = decodeSerial(line, credentials)
            print(response)
            message = encodeSerial(response)
            print(message)
            messageSent = sendSerial(message, ser)
            if messageSent[0] == True:
                print("Sent ", message)
            else:
                print(messageSent[1])
            time.sleep(5)
