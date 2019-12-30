from sense_hat import SenseHat
import time

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

skull1 = [
e,w,e,w,e,w,e,e,
e,w,e,w,e,w,e,e,
w,w,w,w,w,w,w,w,
w,w,w,e,w,w,w,w,
w,y,w,w,w,y,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

skull2 = [
e,w,e,w,e,w,e,e,
e,w,e,w,e,w,e,e,
w,w,w,w,w,w,w,w,
w,w,w,e,w,w,w,w,
w,r,w,w,w,r,w,w,
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

while True:
	sense.set_pixels(skull1)
	time.sleep(.25)
	sense.set_pixels(skull2)
	time.sleep(.25)

