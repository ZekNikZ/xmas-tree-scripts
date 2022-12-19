import time
import board
import neopixel
import sys

NUM_PIXELS = 200

pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, auto_write=False)
pixels.brightness = float(sys.argv[1])

j = 0

while True:
    for i in range(NUM_PIXELS):
        pixels[i] = (255 if (j) % 3 == 0 else 0, 255 if (j ) % 3 == 1 else 0, 255 if (j) % 3 == 2 else 0)
    
    pixels.show()

    time.sleep(0.05)

    j += 1
