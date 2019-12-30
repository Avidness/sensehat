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

crab1 = [
r,e,r,e,r,e,e,e,
r,r,r,r,r,e,r,r,
r,r,r,r,r,r,r,e,
r,r,r,r,r,e,r,r,
e,r,e,e,r,e,e,e,
e,r,e,e,r,e,e,e,
e,w,b,e,w,b,e,e,
e,w,w,e,w,w,e,e
]

crab2 = [
e,r,e,r,e,e,e,e,
r,r,r,r,r,e,r,r,
r,r,r,r,r,r,r,e,
r,r,r,r,r,e,r,r,
e,r,e,e,r,e,e,e,
e,r,e,e,r,e,e,e,
e,w,b,e,w,b,e,e,
e,w,w,e,w,w,e,e
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
	sense.set_pixels(crab1)
	time.sleep(.25)
	sense.set_pixels(crab2)
	time.sleep(.25)

