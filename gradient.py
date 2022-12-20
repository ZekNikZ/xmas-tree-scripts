import time
import neopixel
import colorsys
from constants import *

pixels = neopixel.NeoPixel(pin, num_pixels, pixel_order=neopixel.GRB)
pixels.brightness = 0.6

j = 0

(h, s, v) = (0, 1, 0.5)

while True:
    (r, g, b) = colorsys.hsv_to_rgb((j % 200) / 200, s, v)
    color = (r, g, b)
    color = tuple(map(lambda x: int(x * 255), color))
    pixels.fill(color)

    time.sleep(0.05)

    j += 1
