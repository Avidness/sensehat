from sense_hat import SenseHat
from gpiozero import MotionSensor
import time
import os
import subprocess

r = [255,0,0]
o = [255,165,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]
w = [255,255,255]

cat1 = [
e,r,e,e,e,e,r,e,
r,r,r,e,e,r,r,r,
r,r,r,r,r,r,r,r,
r,w,w,r,r,w,w,r,
r,w,e,r,r,w,e,r,
r,r,r,r,r,r,r,r,
e,r,r,r,r,r,r,e,
e,e,r,r,r,r,e,e
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

sense = SenseHat()
mot = MotionSensor(4)
sense.set_rotation(180)
imagepath = 'public/photo.jpg'

while True:
	if mot.motion_detected:
		print("Motion detected")
		cmd = 'raspistill -o ' + imagepath + ' -t 1000'
		pid = subprocess.call(cmd, shell = True)
		sense.set_pixels(cat1)
	else: 
		print("Nothing detected")
		sense.set_pixels(blank)
	time.sleep(1)
