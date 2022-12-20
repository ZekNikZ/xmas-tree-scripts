import time
import neopixel
import colorsys
from constants import *

pixels = neopixel.NeoPixel(pin, num_pixels, auto_write=False, pixel_order=neopixel.GRB)
pixels.brightness = 0.8

j = 0

(h, s, v) = (0, 1, 0.5)

while True:
    for i in range(num_pixels):
        (r, g, b) = colorsys.hsv_to_rgb(((i + j) % 300) / 300, s, v)
        color = (r, g, b)
        color = tuple(map(lambda x: int(x * 255), color))
        pixels[i] = color

    pixels.show()

    time.sleep(0.025)

    j += 1
