from sense_hat import SenseHat
import curses

sense = SenseHat()
sense.clear(0,0,0)

screen = curses.initscr()
screen.keypad(True)
curses.cbreak()
curses.noecho()

y = 4

sense.set_pixel(0, y, 255, 255, 255)

def drawbat():
	sense.set_pixel(0, y, 255, 255, 255)
	sense.set_pixel(0, y+1, 255, 255, 255)
	sense.set_pixel(0, y-1, 255, 255, 255)

game_over = False

while not game_over:
	drawbat()
	key = screen.getch()
	sense.clear()

	if key == curses.KEY_UP:
		if y > 1:
			y -= 1
	
	if key == curses.KEY_DOWN:
		if y < 6:
			y += 1

