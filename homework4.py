# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:07:05 2018

@author: Connor
"""

import numpy as np           #imports numeric python library
from matplotlib import pyplot as plt #imports required libraries for plotting
import math

def rect(t):                     #returns 1 if abs(parameter) is <.5
    if(np.abs(t)<.5):
        return 1
    else:
        return 0
    
def my_conv(x,h):               #returns a np array holding the convolution of np arrays x and h
    convolution = np.array([])
    h = np.flip(h,0)
    
    for i in range(h.size):
        x = np.insert(x, 0, 0)
        x = np.append(x,0)
    sum = 0
    
    for j in range(x.size-h.size):
        for i in range(h.size):
            sum+=x[i]*h[i]
        h = np.insert(h, 0,0)
        convolution = np.append(convolution, sum)
        sum = 0
    convolution = np.delete(convolution, 0)
    return(convolution)

x = np.array([-2,-1,-.5,-.499, 0, .499, .5, 1, 2])              #plots rect function
y = np.zeros(x.size)
for i in range(x.size):
    y[i] = rect(x[i])

 
sampsPerUnit = 100                                          #creates a variable representing number of samples per unit time

                                 
y1rect = np.array ([])                                      
x1 = np.array([])
counter = 0
for i in range(-2*sampsPerUnit, 2*sampsPerUnit+1):      
    x1 = np.append(x1, i/sampsPerUnit)
    y1rect = np.append(y1rect, rect(x1[counter]))
    counter +=1

y2rect = np.array([])  
x2 = np.array([])
counter = 0
for i in range(-2*sampsPerUnit, 2*sampsPerUnit+1):
    x2 = np.append(x1, i/sampsPerUnit)
    y2rect = np.append(y2rect, rect(x2[counter]/2))
    counter +=1
    
convolution1 = my_conv(y1rect, y1rect)
newx1 = np.array([])
for i in range(int(convolution1.size/-2), int(convolution1.size/2+1)):
    newx1 = np.append(newx1, i/sampsPerUnit)
for j in range(convolution1.size):
    convolution1[j] = convolution1[j]/sampsPerUnit
    
convolution2 = my_conv(y1rect, y2rect)
newx2 = np.array([])
for i in range(int(convolution2.size/-2), int(convolution2.size/2+1)):
    newx2 = np.append(newx2, i/sampsPerUnit)
for j in range(convolution2.size):
    convolution2[j] = convolution2[j]/sampsPerUnit
    
plt.figure(1)
plt.subplot(311)
plt.plot(x,y)
plt.title('Rect() Function')
plt.subplot(312)
plt.plot(newx1, convolution1)
plt.title('y1 = rect(t)*rect(t)')
plt.subplot(313)
plt.plot(newx2, convolution2)
plt.title('y1 = rect(t)*rect(t/2)')
plt.tight_layout()

plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    