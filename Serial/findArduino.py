import warnings
import serial
import serial.tools.list_ports
from arduinoSerialNumbers import arduino as ardser

def findArduino():
	arduino_ports = []
	ports = list(serial.tools.list_ports.comports())
	for p in ports:
		print(p)
		print(p.hwid)
		for entry in p:
			print(entry)
		if ardser in p:
			arduino_ports.append(p.hwid)
	if not arduino_ports:
		return IOError("No Arduino found")
	if len(arduino_ports) > 1:
		warnings.warn("Multiple Arduinos found -- using the first result")
	return arduino_ports[0]

if __name__ == '__main__':
	print(findArduino())
"""
arduino_ports = [
	p.device
	for p in serial.tools.list_ports.comports()
	if 'Arduino' in p.description]
 
print(arduino_ports)
print(serial.tools.list_ports.comports())
if not arduino_ports:
	raise IOError("No Arduino found")
if len(arduino_ports) > 1:
	warnings.warn("Multiple Arduinos found -- using the first result")

print(arduino_ports)
"""
