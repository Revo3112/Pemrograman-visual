import numpy as np
import matplotlib.pyplot as plt

rowmax = int(1079)
colmax = int(1919)

radius_max = int(1000)
batas1 = int(0.2 * radius_max)
batas2 = int(0.4 * radius_max)
batas3 = int(0.8 * radius_max)
batas4 = int(radius_max)

Gambar = np.zeros(shape=(rowmax + 1, colmax + 1, 3), dtype=np.uint8)

for i in range(rowmax + 1):
    for j in range(colmax + 1):
        distance_squared = i**2 + j**2
        
        if distance_squared <= batas1**2:
            Gambar[i, j, 0] = 255
        elif distance_squared <= batas2**2:
            Gambar[i, j, 1] = 255
        elif distance_squared <= batas3**2:
            Gambar[i, j, 2] = 255
        elif distance_squared <= batas4**2:
            Gambar[i, j] = [255, 255, 255]

plt.figure()
plt.imshow(Gambar)
plt.show()
