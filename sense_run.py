from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear(0,0,0)

while True:
	for i in reversed(range(8)):
		for j in reversed(range(8)):
			sense.clear(0,0,0)
			sense.set_pixel(j, i, 255, 0, 0)
			time.sleep(.1)
