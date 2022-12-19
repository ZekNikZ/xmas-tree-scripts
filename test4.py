import time
import board
import neopixel

NUM_PIXELS = 200

pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, auto_write=False)
pixels.brightness = 0.5

j = 0

while True:
    for i in range(NUM_PIXELS):
        if abs(i - j) <= 2:
            pixels[i] = (255, 255, 255)
        else:
            pixels[i] = (0, 0, 0)
    
    pixels.show()

    time.sleep(0.01)

    j += 1
