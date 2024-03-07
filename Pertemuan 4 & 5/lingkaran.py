print("\033c")

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-9, 9, 10000)
plt.figure(figsize=(8, 6.5))

# Menentukan persamaan matematika yang diinginkan 
# persamaan lingkaran x^2 + y^2 = r^2
# persamaan lingkaran (x-a)^2 + (y-b)^2 = r^2
# persamaan lingkaran y = (r^2 - x^2)^0.5
y = x -x -0
y1 = (4-x**2)**0.5
y2 = -(4-x**2)**0.5

y11 = (1.5**2-(x)**2)**0.5
y12 = -(1.5**2-(x)**2)**0.5

y13 = (1.2**2-(x)**2)**0.5
y14 = -(1.2**2-(x)**2)**0.5

y15 = (0.5**2-(x)**2)**0.5
y16 = -(0.5**2-(x)**2)**0.5

y17 = 1.7 + (0.1**2-(x)**2)**0.5
y18 = 1.7 -(0.1**2-(x)**2)**0.5

y3 = 5 + (4-(x-5)**2)**0.5
y4 = 5 - (4-(x-5)**2)**0.5

y5 = -5 + (4-(x+5)**2)**0.5
y6 = -5 - (4-(x+5)**2)**0.5

y7 = 5 + (4-(x+5)**2)**0.5
y8 = 5 - (4-(x+5)**2)**0.5

y9 = -5 + (4-(x-5)**2)**0.5
y10 = -5 - (4-(x-5)**2)**0.5

plt.plot(x,y, '-k')
plt.plot(x, y1,'-r', label='y1,y2')
plt.plot(x, y2,'-r')
# plt.plot(x, y3,'-g', label='y3,y4')
# plt.plot(x, y4,'-g')
# plt.plot(x, y5,'-b', label='y5,y6')
# plt.plot(x, y6,'-b')
# plt.plot(x, y7,'-y', label='y7,y8')
# plt.plot(x, y8,'-y')
# plt.plot(x, y9,'-m', label='y9,y10')
# plt.plot(x, y10,'-m')
plt.plot(x, y11,'-c', label='y11,y12')
plt.plot(x, y12,'-c')
plt.plot(x, y13,'-g', label='y13,y14')
plt.plot(x, y14,'-g')
plt.plot(x, y15,'-b', label='y15,y16')
plt.plot(x, y16,'-b')
plt.plot(x, y17,'-y', label='y17,y18')
plt.plot(x, y18,'-y')
# plt.legend(loc='upper center')
plt.grid()
plt.show()

