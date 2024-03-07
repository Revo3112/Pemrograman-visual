import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import numpy as np

def create_lingkaran(ya, xa, radius, warna, gambar):
    for y in range(int(ya - radius), int(ya + radius) + 1):
        for x in range(int(xa - radius), int(xa + radius) + 1):
            if (x - xa)**2 + (y - ya)**2 <= radius**2:
                if 0 <= y < gambar.shape[0] and 0 <= x < gambar.shape[1]:
                    alpha = 0.6  # Menentukan opacity, bisa disesuaikan
                    gambar[y, x] = (1 - alpha) * gambar[y, x] + alpha * np.array(warna, dtype=np.uint8)  # Mengubah ke tipe data yang benar
    return gambar

radius = 15
warna = (0, 255, 255)
warna_merah = (255, 0, 0)
row = 1500
col = 1500
background_color = (255, 255, 255)
background = np.ones((row, col, 3), dtype=np.uint8)
background[:, :] = background_color
tanda = 0 

for x in range(1001):
    y = 200
    if (x % 100 ==  0):
        for i in range(tanda, x, 10):
            background = create_lingkaran(y, i, radius, warna, background)
        tanda = x
        plt.imshow(background)
        plt.draw()  # Memperbarui plot tanpa menunggu proses plotting selesai
        plt.pause(0.1)

for z in range(y, 1001, 10):
    if (z % 100 ==  0):
        for i in range(tanda, z, 10):
            background = create_lingkaran(i, x, radius, warna, background)
        tanda = z
        plt.imshow(background)
        plt.draw()  # Memperbarui plot tanpa menunggu proses plotting selesai
        plt.pause(0.1)

batas_warna = x
for x in range(x, -1, -10):
    if (x % 100 ==  0):
        for i in range(tanda, x, -10):
            y = (4/5)*i + 200
            background = create_lingkaran(y, i, radius, warna, background)
            for j in range (x , batas_warna + 1, 1):
                background2 = create_lingkaran(y, j, 5, warna_merah, background)
        tanda = x
        plt.imshow(background)
        plt.draw()
        plt.pause(0.1)

tanda = int(y)
y = int(y)
for z in range(200, 1001, 10):
    if (z % 100 ==  0):
        for i in range(tanda, z, 10):
            background = create_lingkaran(i, x, radius, warna, background)
        tanda = z
        plt.imshow(background)
        plt.draw()  # Memperbarui plot tanpa menunggu proses plotting selesai
        plt.pause(0.1)

# Membuat dua garis yang bergerak bersama sama dengan beda arah
tanda1 = x
tanda2 = tanda
y = tanda
x_cor = x
for x in range(x_cor, 1001, 10):
    if (x % 100 ==  0):
        for i in range(tanda1, x, 10):
            tanda2 = (-4/5)*i + 1000
            background = create_lingkaran(y, i, radius, warna, background)
            # background2 = create_lingkaran(tanda2, i, radius, warna, background)
        tanda1 = x
        plt.imshow(background)
        plt.draw()  # Memperbarui plot tanpa menunggu proses plotting selesai
        plt.pause(0.1)


plt.show()  # Menampilkan gambar setelah selesai ditampilkan
