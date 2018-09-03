# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 19:32:28 2018

@author: Connor
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import warnings
np.seterr(divide='ignore', invalid='ignore')
warnings.filterwarnings('ignore')  

b1 = [1, 0, -.64]
a1 = [1, -.8*(2**(1/2)), .64]



w,h = signal.freqz(b1, a1)
z, p, g = signal.tf2zpk(b1, a1)
theta = np.linspace(0,2*np.pi, 101)

fig2 = plt.figure(2)
plt.title('Pole Zero Plot')
theta = np.linspace(0, 2*np.pi, 101)
plt.plot(np.cos(theta), np.sin(theta), 'lightgrey')
plt.plot(z.real, z.imag, 'ko')
plt.plot(p.real, p.imag, 'kx')
plt.ylabel('Imaginary')
plt.xlabel('real')
plt.axes().set_aspect('equal')


fig = plt.figure(1)
plt.title('Frequency and Phase Response')

ax1 = fig.add_subplot(111)
plt.plot(w, abs(h), 'b')
plt.ylabel('|H(e^jw)|', color = 'b')
plt.xlabel('Frequency in rad/s')

ax2 = ax1.twinx()
x = np.angle(h)
plt.plot(w[1:], np.unwrap(x[1:]), 'g')
plt.ylabel('Phase Response', color = 'g')
plt.grid()
plt.axis('tight')

plt.show()
