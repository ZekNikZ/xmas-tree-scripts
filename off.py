import time
import board
import sys
import neopixel

NUM_PIXELS = int(sys.argv[1])

pixels = neopixel.NeoPixel(board.D12, NUM_PIXELS)
pixels.brightness = 0.20

pixels.fill((0, 0, 0))
