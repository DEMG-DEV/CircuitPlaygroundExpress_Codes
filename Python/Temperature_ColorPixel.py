from adafruit_circuitplayground.express import circuit
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
	temp = circuit.temperature
	if temp >= 26.00:
		pixels.fill((255,0,0))
	elif temp < 26.00:
		pixels.fill((0,0,255))
	pixels.write()
	time.sleep(0.5)
	pixels.fill((0,0,0))
	print("Temperatura: %.2f °C" %temp)
	time.sleep(1)