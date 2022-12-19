import time
import board
import neopixel

NUM_PIXELS = 200

pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS)
pixels.brightness = 0.20

while True:
    for i in range(NUM_PIXELS):
        pixels[i] = (255 if i % 3 == 0 else 0, 255 if i % 3 == 1 else 0, 255 if i % 3 == 2 else 0)
        time.sleep(0.01)

    for i in range(NUM_PIXELS):
        pixels[i] = (0, 0, 0)
        time.sleep(0.01)
