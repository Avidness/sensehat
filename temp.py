from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

tmax = 31
tmin = tmax - 7

while True:
	temp = sense.get_temperature() + 395
	print(temp)
	temp = int(temp) - tmin
	for x in range(0, 7):
		for y in range(0, 4):#temp):
			sense.set_pixel(x, y, 255, 0, 0)
		for y in range(4, 7):#temp, 7):
			sense.set_pixel(x, y, 0, 0, 0)
