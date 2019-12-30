#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# pi_camera_options.py
# Takes a sequence of photos with the Pi camera
# using a range of Exposure and White Balance
# settings.
#
# Project URL :
# http://www.raspberrypi-spy.co.uk/?p=1862
#
# Author : Matt Hawkins
# Date   : 21/06/2013
import os
import time
import subprocess
from sense_hat import SenseHat

sense = SenseHat()

r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]
w = [255,255,255]

flash = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

blank = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

photo_interval = 0.25 # Interval between photos (seconds)
photo_counter  = 0    # Photo counter

try:

	print "Starting photo sequence"

	while True:
		sense.set_pixels(flash)
		photo_counter = photo_counter + 1
		filename = 'public/photo.jpg'
		cmd = 'raspistill -o ' + filename + ' -t 1000'
		pid = subprocess.call(cmd, shell=True)
		print ' [' + str(photo_counter) + '] ' + filename  
		#sense.set_pixels(blank)
		time.sleep(photo_interval)
  
except KeyboardInterrupt:
  print 'halting'
