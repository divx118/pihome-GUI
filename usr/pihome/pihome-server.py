#!/usr/bin/env python

# PiHome v1.0
# http://pihome.harkemedia.de/
# 
# PiHome Copyright 2012, Sebastian Harke
# Lizenz Informationen.
# 
# This work is licensed under the Creative Commons Namensnennung - Nicht-kommerziell - Weitergabe unter gleichen Bedingungen 3.0 Unported License. To view a copy of this license,
# visit: http://creativecommons.org/licenses/by-nc-sa/3.0/.


import time
import RPi.GPIO as GPIO
print "starting this"
import cgi,time,string,datetime
from os import curdir, sep, path
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


# Set GPIO Pins
# !! Only Change if you know what you are doing !!
a = 24
b = 25
c = 8
d = 7
on = 18
off = 23
c1 = 17
c2 = 22
c3 = 10
c4 = 9
c5 = 11

# Set to use IO No.
GPIO.setmode(GPIO.BCM)

for gpio_pin in (a, b, c, d, on, off, c1, c2, c3, c4, c5):
  GPIO.setup(gpio_pin, GPIO.OUT)
  GPIO.output(gpio_pin, False)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
        	self.send_response(200)
        	self.send_header('Content-type', 'text/html')
        	self.end_headers()        	
        	
        	datastring = str(self.path).split("request/")[1]        	
        	letter = datastring.split("/")[0]
        	letter = string.upper(letter)
        	status = datastring.split("/")[1]
        	status = string.lower(status)
        	code = datastring.split("/")[2]        	
        	code1 = code[0]
        	code2 = code[1]
        	code3 = code[2]
        	code4 = code[3]
        	code5 = code[4]
        	
        	# Testing
        	#self.wfile.write(datastring)
	       	
	       	if letter != "":
				if letter == "A":
					GPIO.output(a, True)
				elif letter == "B":
					GPIO.output(b, True)
				elif letter == "C":
					GPIO.output(c, True)
				elif letter == "D":
					GPIO.output(d, True)
				
				if status == "on":
					GPIO.output(on, True)
				elif status == "off":
					GPIO.output(off, True)
				
				if code1 == "1":
					GPIO.output(c1, True)
				if code2 == "1":
					GPIO.output(c2, True)
				if code3 == "1":
					GPIO.output(c3, True)
				if code4 == "1":
					GPIO.output(c4, True)
				if code5 == "1":
					GPIO.output(c5, True)
				
				time.sleep(1)
				
				if letter == "A":
					GPIO.output(a, False)
				elif letter == "B":
					GPIO.output(b, False)
				elif letter == "C":
					GPIO.output(c, False)
				elif letter == "D":
					GPIO.output(d, False)
					
				if status == "on":
					GPIO.output(on, False)
				elif status == "off":
					GPIO.output(off, False)
				
				if code1 == "1":
					GPIO.output(c1, False)
				if code2 == "1":
					GPIO.output(c2, False)
				if code3 == "1":
					GPIO.output(c3, False)
				if code4 == "1":
					GPIO.output(c4, False)
				if code5 == "1":
					GPIO.output(c5, False)
				
				time.sleep(0.5)
		return
	except IOError:
		self.send_error(404,'File Not Found: ' + self.path)



def main():
    try:
        srv = HTTPServer(('', 8888), Handler)
        print 'START PiHome SERVER'
        srv.serve_forever()
    except KeyboardInterrupt:
        print ' STOP PiHome SERVER'
        srv.socket.close()


if __name__ == '__main__':
  main()

