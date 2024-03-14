import numpy as np
import matplotlib.pyplot as plt

rowmax = 1079
colmax = 1919
radius_max = 1000

batas1 = int(0.1 * radius_max)
batas2 = int(0.3 * radius_max)
batas3 = int(0.5 * radius_max)
batas4 = int(0.7 * radius_max)
batas5 = int(0.9 * radius_max)
batas6 = radius_max

Gambar = np.zeros(shape=(rowmax + 1, colmax + 1, 3), dtype=np.uint8)

centers = [(0, 0), (0, colmax), (rowmax, 0), (rowmax, colmax)]

for center in centers:
    for i in range(rowmax + 1):
        for j in range(colmax + 1):
            distance_squared = (i - center[0])**2 + (j - center[1])**2

            is_inside_circle_1 = distance_squared <= batas1**2
            is_inside_circle_2 = batas1**2 < distance_squared <= batas2**2
            is_inside_circle_3 = batas2**2 < distance_squared <= batas3**2
            is_inside_circle_4 = batas3**2 < distance_squared <= batas4**2
            is_inside_circle_5 = batas4**2 < distance_squared <= batas5**2
            is_inside_circle_6 = batas5**2 < distance_squared <= batas6**2

            if is_inside_circle_1:
                Gambar[i, j, 0] = 255
            elif is_inside_circle_2:
                Gambar[i, j, 1] = 255
            elif is_inside_circle_3:
                Gambar[i, j, 2] = 255
            elif is_inside_circle_4:
                Gambar[i, j] = [255, 255, 0]
            elif is_inside_circle_5:
                Gambar[i, j] = [255, 0, 255]
            elif is_inside_circle_6:
                Gambar[i, j] = [0, 255, 255]

plt.figure()
plt.imshow(Gambar)
plt.show()
