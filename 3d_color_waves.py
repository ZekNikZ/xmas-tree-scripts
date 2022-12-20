import time
import neopixel
import random
from constants import *
import numpy as np
import sys

WAVE_SIZE = 80 # units
UPDATE_RATE = 0.001 # seconds
MIN_SPEED = 50 # units / second
MAX_SPEED = 60 # units / second
RADIUS = 300
CENTER = np.array([0, 0, 225])
MAX_COLOR = np.array([255, 255, 255])
MIN_COLOR = np.array([0, 0, 0])

def random_unit_vector():
    v = np.random.randn(3) * 2 - 1
    v_hat = v / np.linalg.norm(v)
    return v_hat

def recompute_pixel_t(i):
    global pixel_t
    for vec, _, _, _ in waves:
        pixel_t[i] = list(map(lambda p: vec.dot(p - CENTER) / RADIUS, np_coords))

np_coords = list(map(np.array, coords))

pixels = neopixel.NeoPixel(pin, num_pixels, auto_write=False, pixel_order=neopixel.GRB)
pixels.brightness = 0.5

# (vec, color, speed, t)
waves = [
    [random_unit_vector(), MAX_COLOR, MIN_SPEED, -1]
]
pixel_t = [None for _ in waves]
for i in range(len(waves)):
    recompute_pixel_t(i)

while True:
    s = time.time_ns()
    for i in range(num_pixels):
        color = np.array([0, 0, 0])

        for j, (vec, col, speed, t) in enumerate(waves):
            brightness = min(1, max(0, 1 - 2 * abs(pixel_t[j][i] - t) * RADIUS / WAVE_SIZE))
            color = color + col * brightness

        pixels[i] = tuple(map(int, np.maximum(np.minimum(color, MAX_COLOR), MIN_COLOR)))
    
    pixels.show()

    time.sleep(UPDATE_RATE)
    td = time.time_ns() - s

    # Update waves
    for i, wave in enumerate(waves):
        waves[i][3] = t + 2 * wave[2] / RADIUS * (td / 1000000000)
        if waves[i][3] > 1:
            waves[i] = [random_unit_vector(), MAX_COLOR, MIN_SPEED, -1]
            recompute_pixel_t(i)
