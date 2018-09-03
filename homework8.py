# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:35:35 2018

@author: Connor
"""
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')   #becayse I kept getting a complex warning 
#when plotting y(t) even through the imaginary part was 0

w1 = np.logspace(-2, 4, 100)

def abshjw(w):
    return(1/(np.sqrt(25+(.2*w-(10/w))**2)))

plt.figure(1)
plt.semilogx(w1, 20*np.log10(abshjw(w1)))
plt.xlabel('w')
plt.ylabel('|H(jw)| in dB')
plt.show()

x = np.linspace(0,20,num=500)
k = np.linspace(-20, 20, 41)
y = np.zeros(500, dtype=complex)
count = 0

def hjw(w):
    j= 0+1j
    return((j*w)/(-.2*w**2+j*5*w+10))
def ak(k):
   j = 0+1j
   return((5/(k*np.pi))*(np.exp(-j*k*(np.pi/10)))*(np.sin((k*np.pi)/10)))
def bk(k):
    j = 0+1j
    return(ak(k)*hjw(k*((np.pi)/5)))

for t in x:
    for k1 in k:
        if k1!=0:
            j = 0+1j
            y[count] = y[count]+bk(k1)*np.exp(j*k1*np.pi/5*t)
    count += 1
        
plt.figure(2)
plt.plot(x,y.real)
plt.xlabel('time (msec)')
plt.ylabel('y(t) (Amps)')
plt.show()



