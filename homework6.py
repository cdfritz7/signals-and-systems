# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 10:11:25 2018

@author: Connor
"""

import numpy as np           #imports numeric python library
from matplotlib import pyplot as plt #imports required libraries for plotting


k2 = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
sixABkArray = np.zeros(9)
for i in range(9):
    if(k2[i]!=0):
        sixABkArray[i] = (1/(2*np.pi*k2[i]))*np.sin((np.pi*k2[i])/2)
sixABkArray[4] = 3/4

sixACkArray = np.zeros(9)
for i in range(9):
    if(k2[i]!=0):
        sixACkArray[i] = (1/(2*np.pi*k2[i]))*np.cos((np.pi*k2[i])/2) + (1/(2*np.pi*k2[i]))*np.cos((np.pi*k2[i])) - 1/(k2[i]*np.pi)
sixACkArray[4] = 0

sixBBkArray = np.zeros(9)
for i in range(9):
    if(k2[i]!=0):
        sixBBkArray[i] = 0
sixBBkArray[4] = 0

sixBCkArray = np.zeros(9)
for i in range(9):
    if(k2[i]!=0):
        sixBCkArray[i] = (1/(np.pi*k2[i]))*(np.cos((np.pi*k2[i])/3)-np.cos((2*np.pi*k2[i])/3))
sixACkArray[4] = 0

plt.figure(1)
plt.subplot(411)
plt.stem(k2, sixABkArray)
plt.title('Problem 6A Real Fourier Coefficients')
plt.subplot(412)
plt.stem(k2, sixACkArray)
plt.title('Problem 6A Imaginary Fourier Coefficients')
plt.subplot(413)
plt.stem(k2, sixBBkArray)
plt.title('Problem 6B Real Fourier Coefficients')
plt.subplot(414)
plt.stem(k2, sixBCkArray)
plt.title('Problem 6B Imaginary Fourier Coefficients')

plt.tight_layout()
