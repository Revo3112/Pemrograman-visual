import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-9, 9, 10000)

plt.figure(figsize=(8, 6.5))

# Menentukan persamaan matematika yang diinginkan
# persamaan lingkaran x^2 + y^2 = r^2
# persamaan lingkaran (x-a)^2 + (y-b)^2 = r^2
# persamaan lingkaran y = (r^2 - x^2)^0.5

# Membuat kepala dengan radius 5 dan titik pusat (5, 5)
y1 = 5 + (5 - (x - 5)**2)**0.5
y2 = 5 - (5 - (x - 5)**2)**0.5

# membuat telinga dengan radisu 2 dan titik pusat (3, 7)
y3 = 7 + (2 - (x - 3)**2)**0.5
y4 = 7 - (2 - (x - 3)**2)**0.5

# membuat telinga dengan radisu 2 dan titik pusat (7, 7)
y5 = 7 + (2 - (x - 7)**2)**0.5
y6 = 7 - (2 - (x - 7)**2)**0.5

# membuat mata dengan radius 0.5 dan titik pusat (4.5, 5) dalam bentuk elips
# y7 = 5 + (0.5 - (x - 4)**2)**0.5
# y8 = 5 - (0.5 - (x - 4)**2)**0.5   
y7 = 0.6 * np.sqrt(1 - (x - 4.5)**2 / 0.3**2) + 5
y8 = -0.6 * np.sqrt(1 - (x - 4.5)**2 / 0.3**2) + 5

# # membuat mata dengan radius 0.5 dan titik pusat (6, 5) dalam bentuk elips
# y9 = 5 + (0.5 - (x - 6)**2)**0.5
# y10 = 5 - (0.5 - (x - 6)**2)**0.5
y9 = 0.6 * np.sqrt(1 - (x - 5.5)**2 / 0.3**2) + 5
y10 = -0.6 * np.sqrt(1 - (x - 5.5)**2 / 0.3**2) + 5

# Membuat bola mata dengan radius 0.2 dan titik pusat (4.66, 5)
y11 = 4.66 + (0.08 - (x - 4.5)**2)**0.5
y12 = 4.66 - (0.08 - (x - 4.5)**2)**0.5

# Membuat bola mata dengan radius 0.2 dan titik pusat (4.66, 5)
y13 = 4.66 + (0.08 - (x - 5.5)**2)**0.5
y14 = 4.66 - (0.08 - (x - 5.5)**2)**0.5

# membuat hidung dengan radius 0.5 dan titik pusat (5, 4)
y15 = 4 + (0.2 - (x - 5)**2)**0.5
y16 = 4 - (0.2 - (x - 5)**2)**0.5

plt.plot(x, y1, '-k', label='y1, y2')
plt.plot(x, y2, '-k')
plt.plot(x, y3, '-k', label='y3, y4')
plt.plot(x, y4, '-k')
plt.plot(x, y5, '-k', label='y5, y6')
plt.plot(x, y6, '-k')
plt.plot(x, y7, '-k', label='y7, y8')
plt.plot(x, y8, '-k')
plt.plot(x, y9, '-k', label='y9, y10')
plt.plot(x, y10, '-k')
plt.plot(x, y11, '-k', label='y11, y12')
plt.plot(x, y12, '-k')
plt.plot(x, y13, '-k', label='y13, y14')
plt.plot(x, y14, '-k')
plt.plot(x, y15, '-k', label='y15, y16')
plt.plot(x, y16, '-k')
plt.fill_between(x, y1, y2, color='black', alpha=1)
plt.fill_between(x, y3, y4, color='black', alpha=1)
plt.fill_between(x, y5, y6, color='black', alpha=1)
plt.fill_between(x, y7, y8, color='white', alpha=1)
plt.fill_between(x, y9, y10, color='white', alpha=1)
plt.fill_between(x, y11, y12, color='black', alpha=1)
plt.fill_between(x, y13, y14, color='black', alpha=1)
plt.fill_between(x, y15, y16, color='red', alpha=1)
plt.show()