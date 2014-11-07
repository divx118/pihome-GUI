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
import cgi,time,string,datetime,re
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
        	datastring = str(self.path).split("request/")[1].split("/")
                # Check the received string
                if bool(re.match("[a-d]", string.lower(datastring[0]), flags = 0)):
                  letter = eval(string.lower(datastring[0]))
                  if bool(re.match("^(on|off)$", string.lower(datastring[1]), flags = 0)):
        	    status = eval(string.lower(datastring[1]))
        	    if bool(re.match("^([0-1]{5})$",datastring[2],flags = 0)):
                      # Set the right GPIO pins high
                      i = 1
                      for code in datastring[2]:
                        GPIO.output(eval("c" + str(i)), bool(int(code)))
                        i+=1
                      GPIO.output(letter, True)
                      GPIO.output(status, True)
                      # Time to send the signal
                      time.sleep(1)
                      # Set all used GPIO pins low again
                      i = 1
                      for code in datastring[2]:
                        GPIO.output(eval("c" + str(i)), False)
                        i+=1
                      GPIO.output(letter, False)
                      GPIO.output(status, False)     					
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

