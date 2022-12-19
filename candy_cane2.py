import time
import board
import neopixel
import colorsys
import random
from coords import coords
import math

NUM_PIXELS = 300
DELAY = 0.01 # seconds
ROTATION_PERIOD = 2 # seconds
TWIST_PERIOD = 1.5

pixels = neopixel.NeoPixel(board.D12, NUM_PIXELS, auto_write=False)
pixels.brightness = 1

t = 0
while True:
    for i in range(NUM_PIXELS):
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
    
