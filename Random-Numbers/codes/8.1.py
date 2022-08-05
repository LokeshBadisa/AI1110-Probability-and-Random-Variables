# Plotting Y = AX + N

# Name: Lokesh Badisa
# Roll number: AI21BTECH11005

import numpy as np
import matplotlib.pyplot as plt

Y = np.loadtxt('codes/8.1.dat', dtype='double')
X = np.loadtxt('codes/ber2d.dat', dtype='int')

plt.plot(Y[X[:, 0] == 1, 0], Y[X[:, 0] == 1, 1], 'o', label='$\mathbf{y}|\mathbf{s}_0$')
plt.plot(Y[X[:, 0] == 0, 0], Y[X[:, 0] == 0, 1], 'o', label='$\mathbf{y}|\mathbf{s}_1$')
plt.grid()
plt.legend()
plt.xlabel('$y_1$')
plt.ylabel('$y_2$')
plt.savefig('figs/8.1.png')
plt.show()
