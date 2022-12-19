import time
import board
import neopixel
import colorsys

NUM_PIXELS = 300
# NUM_PIXELS = 100

pixels = neopixel.NeoPixel(board.D12, NUM_PIXELS, auto_write=False)
# pixels = neopixel.NeoPixel(board.D12, NUM_PIXELS, auto_write=False)
pixels.brightness = 0.8

j = 0

(h, s, v) = (0, 1, 0.5)

while True:
    for i in range(NUM_PIXELS):
        (r, g, b) = colorsys.hsv_to_rgb(((i + j) % 300) / 300, s, v)
        color = (r, g, b)
        color = tuple(map(lambda x: int(x * 255), color))
        pixels[i] = color

    pixels.show()

    time.sleep(0.025)

    j += 1
