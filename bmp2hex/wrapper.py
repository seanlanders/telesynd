#!/usr/bin/env python

##@file wrapper.py
# A wrapper for ease of using bmp2hex.
# Used as a means of converting 1-bit JPG -> BMP -> hex,
# later uploaded to an Arduino, to be displayed on a CRT
# using TV-out.
#
#	~~~
#
#   Anti-Copyright License:
#	This code is Copyrighted in U.S., under MIT Opensource License, 
#   and anybody caught usin it without our permission, 
#   will be mighty good friends of ourn, cause we don't give a dern.
# 
#   Publish it. Write it. Sing it. Swing to it. Yodel it. 
#   We wrote it, that's all we wanted to do.
#   S. Landers (sean.landers@gmail.com) 09-09-2020
#	~~~


import bmp2hex as b2h
import glob

def write2hex(file, prefix, outfile):
	write = b2h.bmp2hex(file, 16, 0, True, True, False, False, False, prefix)
	write = write.encode()
	try:
		with open(outfile, "wb") as binary_file:
			binary_file.write(write)
			binary_file.close()
	except:
		pass

def makeHfile(outfile, variable):
	output = "#include <avr/pgmspace.h>\n"
	output += "#ifndef " + variable.upper() + "_H\n"
	output += "#define " + variable.upper() + "_H\n"
	output += "\nextern const unsigned char " + variable + "[];\n"
	output += "#endif"
	filename = outfile + ".h"
	with open(filename, "w") as f:
		f.write(output)
		f.close()

if __name__ == "__main__":
	writeFiles = glob.glob('*.bmp')
	for file in writeFiles:
		print(file)
		prefix = file.split('.')
		prefix = prefix[0]
		print(prefix)
		outfile = prefix + ".cpp"
		write2hex(file, prefix, outfile)
		makeHfile(prefix, prefix)