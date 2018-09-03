# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 12:15:58 2018

@author: Connor
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
from IPython.display import Audio
import os

[fs,funky] = wavfile.read('funky (1).wav')  #10th order butterworth lowpass filter to suppress frequencies higher than 200 Hz

fNormLow = 200/(fs/2)
b1, a1 = signal.butter(10, fNormLow, 'lowpass')
funkylow = signal.filtfilt(b1, a1, funky)

fNormHigh = 5000/(fs/2) #highpass filter 5kHz
b2, a2 = signal.butter(10, fNormHigh, 'highpass')
funkyHigh = signal.filtfilt(b2, a2, funky)

fNormBandLow = 1000/(fs/2)  #BandPass Filter 1k-2.5kHz
fNormBandHigh = 2500/(fs/2)
b3, a3 = signal.butter(10, [fNormLow, fNormHigh], 'bandpass')
funkyBand = signal.filtfilt(b3, a3, funky)


#plot the frequency response of the lowpass signal
w, h = signal.freqz(b1, a1, 128, fs) #The number 128 is a parameter
#related to the sampling of the frequency response

plt.subplot(211)
plt.title('frequency response of lowpass signal')
plt.plot(w, 20*np.log(np.absolute(h)))
plt.subplot(212)
plt.plot(w, np.angle(h))
plt.show()

#plot the spectrum of the lowpass output signal

f, Pxx_den = signal.periodogram(funkylow, fs)
plt.semilogx(f, Pxx_den)
plt.grid()
plt.xlim(10, 10**4)
plt.title('Lowpass Spectrum')
plt.show()
print('In the lowpass filter case, the filter is attenuating frequencies higher than 200 hz. Consequently, the filter lets the lower frequencies \'pass\' and removes higher frequencies. This makes the lower notes, or bass, in the music more prominent, and removes some of the higher notes.')

#play the output signal
Audio(funkylow, rate=fs)



#plot the frequency response of the highpass signal
w, h = signal.freqz(b2, a2, 128, fs) #The number 128 is a parameter
#related to the sampling of the frequency response

plt.subplot(211)
plt.title('frequency response of highpass signal')
plt.plot(w, 20*np.log(np.absolute(h)))
plt.subplot(212)
plt.plot(w, np.angle(h))
plt.show()

#plot the spectrum of the highpass output signal

r, Pxx_den = signal.periodogram(funkyHigh, fs)
plt.semilogx(r, Pxx_den)
plt.grid()
plt.xlim(10, 10**4)
plt.title('Highpass Spectrum')
plt.show()
print('In the highpass filter case, the filter is attenuating frequencies lower than 5000 hz. Consequently, the filter lets higher frequencies \'pass\' and removes lower frequencies. This makes the higher, or treble, notes in the song more prominent and removes some of the bass')
#play the output signal
Audio(funkyHigh, rate=fs)

#plot the frequency response of the bandpass signal
w, h = signal.freqz(b3, a3, 128, fs) #The number 128 is a parameter
#related to the sampling of the frequency response

plt.subplot(211)
plt.title('frequency response of bandpass signal')
plt.plot(w, 20*np.log(np.absolute(h)))
plt.subplot(212)
plt.plot(w, np.angle(h))
plt.show()

#plot the spectrum of the bandpass output signal

s, Pxx_den = signal.periodogram(funkyBand, fs)
plt.semilogx(s, Pxx_den)
plt.grid()
plt.xlim(10, 10**4)
plt.title('Bandpass Spectrum')
plt.show()
print('In the bandpass filter case, the filter is attenuating frequencies lower than lower than 1000 hz and higher than 2500 Hz. Consequently, the filter frequencies within this range \'pass\'. This has the effect of removing both the bass and high notes, and makes the music sound somewhat muffled')
#play the output signal
Audio(funkyBand, rate=fs)

