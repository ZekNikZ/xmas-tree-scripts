import time
import neopixel
import colorsys
import random
from constants import *
import math

DELAY = 0.01 # seconds
ROTATION_PERIOD = 2 # seconds
TWIST_PERIOD = 1.5

pixels = neopixel.NeoPixel(pin, num_pixels, auto_write=False, pixel_order=neopixel.GRB)
pixels.brightness = 1

t = 0
while True:
    for i in range(num_pixels):
        angle = math.atan2(coords[i][1], coords[i][0]) + math.pi
        angle += coords[i][2] / 450 * 2 * math.pi * TWIST_PERIOD
        if ROTATION_PERIOD > 0:
            angle += t * DELAY / ROTATION_PERIOD * math.pi * 8
        angle %= 2 * math.pi
        if angle < math.pi / 2:
            pixels[i] = (0, 255, 0)
        elif angle < math.pi:
            pixels[i] = (255, 0, 0)
        else:
            pixels[i] = (128,) * 3

    t += 1

    pixels.show()

    time.sleep(DELAY)
    
