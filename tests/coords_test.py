import time
import board
import neopixel
import colorsys
import random
import coords

NUM_PIXELS = 300
DELAY = 0.05 # seconds

pixels = neopixel.NeoPixel(board.D12, NUM_PIXELS, auto_write=False)
pixels.brightness = 1

for coord in coords.coords:
    print(*coord)

for i in range(NUM_PIXELS):
    if coords.coords[i][2] <= 225:
        pixels[i] = (255, 0, 0)
    else:
        pixels[i] = (0, 255, 0)

pixels.show()
    
