import pygame.camera
import pygame.image
import sys
import board
import neopixel
import time
import os

pygame.camera.init()

cameras = pygame.camera.list_cameras()
# camera = pygame.camera.Camera(cameras[0], (1920, 1080))
camera = pygame.camera.Camera(cameras[0])

folder_name = input("Folder name: ")
num_pixels = int(input("Num pixels: "))

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
else:
    print("Folder already exists")
    sys.exit(1)

pixels = neopixel.NeoPixel(board.D12, num_pixels, auto_write=False)
pixels.brightness = 1

for current in range(num_pixels):
    for i in range(num_pixels):
        if current == i:
            pixels[i] = (255, 255, 255)
        else:
            pixels[i] = (0, 0, 0)

    pixels.show()

    time.sleep(0.5)
    
    camera.start()
    camera.get_image()
    camera.get_image()
    img = camera.get_image()
    camera.stop()
    pygame.image.save(img, f"{folder_name}/pixel_{current:03d}.bmp")
    print(f"[{current:03d}/{num_pixels:03d}] Wrote to {folder_name}/pixel_{current:03d}.bmp")

    time.sleep(0.5)
