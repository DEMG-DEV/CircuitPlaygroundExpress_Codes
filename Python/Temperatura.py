from adafruit_circuitplayground.express import circuit
import time

while True:
	temp = circuit.temperature
	print("Temperatura: %.2f °C" %temp)
	time.sleep(1)