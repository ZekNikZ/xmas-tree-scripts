import board

# Pin
pin = board.D12

# Number of pixels
num_pixels = 300

# Coordinates
coords = []
with open('coords.txt', 'r') as f:
    for line in f:
        i, x, y, z = map(float, line.strip().split())
        coords.append((x, y, z))

