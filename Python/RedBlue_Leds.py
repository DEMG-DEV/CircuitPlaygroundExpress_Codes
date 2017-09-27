import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
	pixels.fill((255,0,0))
	pixels.write()
	time.sleep(0.5)
	pixels.fill((0,0,255))
	pixels.write()
	time.sleep(0.5)