import time
import sys
import neopixel
from constants import *

pixels = neopixel.NeoPixel(pin, num_pixels)
pixels.brightness = 0.20

pixels.fill((0, 0, 0))
