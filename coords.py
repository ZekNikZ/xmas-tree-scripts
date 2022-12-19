coords = []

with open('coords.txt', 'r') as f:
    for line in f:
        i, x, y, z = map(float, line.strip().split())
        coords.append((x, y, z))
