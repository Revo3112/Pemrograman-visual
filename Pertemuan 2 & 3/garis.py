print("\033c")
import numpy as np
import matplotlib.pyplot as plt

# Tentukan wilayah (domain) diagram cartesian dan rasio lebar dan tinggi diagram 
x = np.linspace(-50, 50, 100)

# Tentukan persamaan matematika yang diinginkan 
y1 = x - x
y2 = 0.5 * x
y3 = x
y4 = x**2
y5 = x**3
y6 = -2 * x
y7 = x + 2

# Hitung titik tengah dari pertemuan semua garis
x_midpoint = 0
y_midpoint = 0

# Background putih
gambar = np.ones((100, 100, 3), dtype=np.uint8) * 255

# Draw Circle in the middle
plt.plot(x_midpoint, y_midpoint, 'o', color='black', markersize=20)

# Plot semua garis
plt.plot(x, y1, '-r', label='y = 0')
plt.plot(x, y2, '-g', label='y = 0.5x')
plt.plot(x, y3, '-b', label='y = x')
plt.plot(x, y4, '-c', label='y = x^2')
plt.plot(x, y5, '-m', label='y = x^3')
plt.plot(x, y6, '-y', label='y = -2x')
plt.plot(x, y7, '-k', label='y = x + 2')

# Menampilkan lingkaran di latar belakang
plt.imshow(gambar, extent=[-50, 50, -50, 50])

plt.xlim(-50, 50)  # Menyesuaikan rentang sumbu x
plt.ylim(-50, 50)  # Menyesuaikan rentang sumbu y

plt.legend(loc='upper left')
plt.grid()
plt.show()


# Mencari persamaan garis
def persamaan_garis(x1, y1, x2, y2):
    def garis(x):
        return ((y2 - y1) / (x2 - x1)) * (x - x1) + y1

    return garis

Koordinat_x1 = [2, 4]
Koordinat_y1 = [1, 2]

Koordinat_x2 = [8, 10]
Koordinat_y2 = [2, 4]

# Mencari persamaan garis
y1 = persamaan_garis(Koordinat_x1[0], Koordinat_y1[0], Koordinat_x1[1], Koordinat_y1[1])
y2 = persamaan_garis(Koordinat_x2[0], Koordinat_y2[0], Koordinat_x2[1], Koordinat_y2[1])

print ("Persamaan garis pertama: y = " + str(y1))
# Menyusun data untuk plot
x_values = [x for x in range(min(Koordinat_x1[0], Koordinat_x2[0]), max(Koordinat_x1[1], Koordinat_x2[1]) + 1)]
y_values1 = [y1(x) for x in x_values]
y_values2 = [y2(x) for x in x_values]

# Plot garis pertama
plt.plot(x_values, y_values1, '-r', label="Garis Satu")

# Plot garis kedua
plt.plot(x_values, y_values2, '-b', label="Garis Dua")

# Menampilkan plot
plt.legend()
plt.show()