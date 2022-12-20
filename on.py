import time
import sys
import neopixel
from constants import *

pixels = neopixel.NeoPixel(pin, num_pixels)
pixels.brightness = 1

pixels.fill((255, 255, 255))
