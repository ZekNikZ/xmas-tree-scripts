import time
import board
import neopixel

NUM_PIXELS = 200

pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS)
pixels.brightness = 0.20

while True:
    pixels.fill((255, 255, 255))

    time.sleep(0.5)

    pixels.fill((0, 0, 0))

    time.sleep(0.5)
