import time
import neopixel
import random
from constants import *

DELTA = 80
MIN_SPEED = 1
MAX_SPEED = 6

pixels = neopixel.NeoPixel(pin, num_pixels, auto_write=False, pixel_order=neopixel.GRB)
pixels.brightness = 1

j1 = 0
j2 = 0
j3 = 0
a1 = 2
a2 = 4
a3 = 6

while True:
    for i in range(num_pixels):
        r = max(0, min((DELTA - abs(i - j1)) / DELTA * 255, 255))
        g = max(0, min((DELTA - abs(i - j2)) / DELTA * 255, 255))
        b = max(0, min((DELTA - abs(i - j3)) / DELTA * 255, 255))
        pixels[i] = (r, g, b)
    
    pixels.show()

    time.sleep(0.05)

    j1 += a1
    j2 += a2
    j3 += a3

    if j1 < 0 or j1 > num_pixels:
        a1 = random.randint(MIN_SPEED, MAX_SPEED) * -a1 / abs(a1)
        j1 = max(0, min(num_pixels, j1))
    if j2 < 0 or j2 > num_pixels:
        a2 = random.randint(MIN_SPEED, MAX_SPEED) * -a2 / abs(a2)
        j2 = max(0, min(num_pixels, j2))
    if j3 < 0 or j3 > num_pixels:
        a3 = random.randint(MIN_SPEED, MAX_SPEED) * -a3 / abs(a3)
        j3 = max(0, min(num_pixels, j3))
