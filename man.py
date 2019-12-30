from sense_hat import SenseHat
import time

sense = SenseHat()

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
w,w,w,w,w,w,w,w,
e,e,e,w,e,e,e,w,
e,r,e,w,e,r,e,w,
e,e,e,w,e,e,e,w,
w,w,w,w,w,w,w,w,
e,w,e,w,e,w,w,w,
e,w,e,w,e,w,w,w,
w,w,w,w,w,w,w,w
]

cat2 = [
e,r,e,e,e,e,r,e,
r,r,r,e,e,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,w,e,r,r,w,e,r,
r,r,r,r,r,r,r,r,
e,r,r,r,r,r,r,e,
e,e,r,r,r,r,e,e
]

cat3 = [
e,r,e,e,e,e,r,e,
r,r,r,e,e,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
e,r,r,r,r,r,r,e,
e,e,r,r,r,r,e,e
]

crab2 = [
y,e,y,e,y,e,y,e,
y,w,v,g,b,i,e,e,
y,y,y,y,y,y,y,e,
y,y,y,y,y,y,y,y,
y,e,y,y,y,r,y,r,
y,e,e,e,y,y,y,y,
y,e,e,e,y,e,e,o,
e,y,e,e,e,e,e,e
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
	sense.set_rotation(180)
	sense.set_pixels(cat1)
	time.sleep(5)
	sense.set_pixels(cat2)
	time.sleep(.1)
	sense.set_pixels(cat3)
	time.sleep(.25)
	sense.set_pixels(cat2)
	time.sleep(.1)

