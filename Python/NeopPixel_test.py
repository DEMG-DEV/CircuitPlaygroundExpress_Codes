import neopixel
from board import *
import time

RED = 0x100000 # (0x10, 0, 0) also works

# Using `with` ensures pixels are cleared after we're done.
with neopixel.NeoPixel(NEOPIXEL, 10) as pixels:
    pixels[::2] = [RED] * (len(pixels) // 2)
    time.sleep(2)