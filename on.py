import time
import board
import sys
import neopixel

NUM_PIXELS = int(sys.argv[1])

pixels = neopixel.NeoPixel(board.D12, NUM_PIXELS)
pixels.brightness = 1

pixels.fill((255, 255, 255))
