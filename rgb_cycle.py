import time
import neopixel
from constants import *

pixels = neopixel.NeoPixel(pin, num_pixels, auto_write=False, pixel_order=neopixel.GRB)
pixels.brightness = 1

j = 0

while True:
    for i in range(num_pixels):
        pixels[i] = (255 if (i + j) % 3 == 0 else 0, 255 if (i + j) % 3 == 1 else 0, 255 if (i + j) % 3 == 2 else 0)
    
    pixels.show()

    time.sleep(0.3)

    j += 1
