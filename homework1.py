# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 20:36:06 2018

@author: Connor Fritz
"""

import numpy as np           #imports numeric python library
from matplotlib import pyplot as plt #imports required libraries for plotting

dt = 1/1000                 #time increment
t = np.arange(-1,1,dt)     #vector [-1, -.99,...]
f0=4                       #frequency
x = 100 * np.real(np.exp(1j*(2*np.pi*f0*(t - .75))));

plt.subplot(3,1,1)          #creates a 3x1 array of plots
                            #selecting the first one
plt.plot(t,x)               #Draw the plot
plt.title('Section of a Sinusoid') #Add the title
plt.xlabel('time (sec)')        #Add label for x axis
plt.show()                      #Pull up the plot