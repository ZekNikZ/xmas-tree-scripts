import time
import board
import neopixel
import colorsys
import random

NUM_PIXELS = 300
COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 69, 0),
    (0, 255, 255),
    (255, 255, 0),
    (255, 0, 255)
]
DELAY = 0.05 # seconds
MIN_FLICKER_TIME = 0.5 # seconds
MAX_FLICKER_TIME = 2 # seconds

# Calculations
MIN_FLICKER_TIME = int(MIN_FLICKER_TIME / DELAY)
MAX_FLICKER_TIME = int(MAX_FLICKER_TIME / DELAY)
INITIAL_TIME = int(3 / DELAY)

pixels = neopixel.NeoPixel(board.D12, NUM_PIXELS, auto_write=False)
pixels.brightness = 1

data = [[(0, 0, 0), INITIAL_TIME, INITIAL_TIME, (255, 255, 255)] for _ in range(NUM_PIXELS)]

while True:
    for i in range(NUM_PIXELS):
        pixel_data = data[i]
        old_color, counter, max_counter, new_color = pixel_data

        r = int((new_color[0] - old_color[0]) * ((max_counter - counter) / max_counter) + old_color[0])
        g = int((new_color[1] - old_color[1]) * ((max_counter - counter) / max_counter) + old_color[1])
        b = int((new_color[2] - old_color[2]) * ((max_counter - counter) / max_counter) + old_color[2])

        color = (r, g, b)
        pixels[i] = color

        data[i][1] -= 1

        if data[i][1] < 0:
            new_counter = random.randint(MIN_FLICKER_TIME, MAX_FLICKER_TIME)
            data[i] = [new_color, new_counter, new_counter, random.choice(COLORS)]

    pixels.show()

    time.sleep(DELAY)
