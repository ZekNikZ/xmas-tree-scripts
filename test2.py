import time
import board
import neopixel

NUM_PIXELS = 300

pixels = neopixel.NeoPixel(board.D12, NUM_PIXELS, auto_write=False)
pixels.brightness = 1

j = 0

while True:
    for i in range(NUM_PIXELS):
        pixels[i] = (255 if (i + j) % 3 == 0 else 0, 255 if (i + j) % 3 == 1 else 0, 255 if (i + j) % 3 == 2 else 0)
    
    pixels.show()

    time.sleep(0.3)

    j += 1
