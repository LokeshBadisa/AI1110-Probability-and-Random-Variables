# Loads the gau.dat file and plots the empirical and theoretical PDF of the Gaussian random variable in [-6,6]

# Name: Lokesh Badisa
# Roll number: AI21BTECH11005

import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

values = np.loadtxt('codes/gau.dat', dtype='double')
NUM = len(values)
X1 = np.linspace(-7, 7, 30)
X2 = np.linspace(-7, 7, 100)
emp_cdf = []
emp_pdf = [0]
the_pdf = []

for x in X1:
    count = 0
    for value in values:
        if value <= x:
            count += 1
    emp_cdf.append(count/NUM)

for i in range(len(X1)-1):
    emp_pdf.append((emp_cdf[i+1] - emp_cdf[i]) / (X1[i+1] - X1[i]))

def gaussPDF(x):
    return np.exp(-0.5 * (x**2)) / (2 * np.pi)**0.5

for x in X2:
    the_pdf.append(gaussPDF(x))

plt.plot(X2, the_pdf, label='Theoretical')
plt.plot(X1, emp_pdf, 'o', label='Empirical')
plt.grid()
plt.legend()
plt.savefig('figs/2.3.png')
plt.show()
