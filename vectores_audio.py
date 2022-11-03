# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 21:49:02 2022

@author: Adrian
"""

import numpy as np
import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import scipy.fftpack as fourier

# #Señal en el dominio de la frecuencia
def furier(file):
    fs, data=waves.read(file)
    audio=data[:,0]
    L=len(audio)
    T=1/fs
    spec=np.abs(fourier.fft(audio))[:L//2]
    freq=fourier.rfftfreq(L//2,T)[:L//2]
    return spec
    # plt.figure(1)
    # plt.plot(freq, spec)
    # plt.title('Dominio de la frecuencia palabra: "auto"')
    # plt.xlabel('Frecuencia [Hz]')
    # plt.ylabel('Amplitud')



def audiosPalabra1():
    palabra1 = []

    palabra1.append(furier("auto.wav"))
    palabra1.append(furier("auto1.wav"))
    palabra1.append(furier("auto2.wav"))
    palabra1.append(furier("auto3.wav"))
    palabra1.append(furier("auto4.wav"))
    palabra1.append(furier("auto5.wav"))
    palabra1.append(furier("auto6.wav"))
    palabra1.append(furier("auto7.wav"))
    palabra1.append(furier("auto8.wav"))
    palabra1.append(furier("auto9.wav"))

    return palabra1

audiosPalabra1()

def audiosPalabra2():
    palabra2 = []
    
    palabra2.append(furier("observar.wav"))
    palabra2.append(furier("observar1.wav"))
    palabra2.append(furier("observar2.wav"))
    palabra2.append(furier("observar3.wav"))
    palabra2.append(furier("observar4.wav"))
    palabra2.append(furier("observar5.wav"))
    palabra2.append(furier("observar6.wav"))
    palabra2.append(furier("observar7.wav"))
    palabra2.append(furier("observar8.wav"))
    palabra2.append(furier("observar9.wav"))
    
    return palabra2

def audiosPalabra3():
    palabra3 = []
    
    palabra3.append(furier("neurodifuso.wav"))
    palabra3.append(furier("neurodifuso1.wav"))
    palabra3.append(furier("neurodifuso2.wav"))
    palabra3.append(furier("neurodifuso3.wav"))
    palabra3.append(furier("neurodifuso4.wav"))
    palabra3.append(furier("neurodifuso5.wav"))
    palabra3.append(furier("neurodifuso6.wav"))
    palabra3.append(furier("neurodifuso7.wav"))
    palabra3.append(furier("neurodifuso8.wav"))
    palabra3.append(furier("neurodifuso9.wav"))
    
    return palabra3

def audiosPrueba():
    prueba1 = []
    prueba2 = []
    prueba3 = []
    
    prueba1.append(furier("auto.wav"))
    prueba1.append(furier("auto9.wav"))
    
    prueba2.append(furier("observar.wav"))
    prueba1.append(furier("observar9.wav"))
    
    prueba3.append(furier("neurodifuso.wav"))
    prueba3.append(furier("neurodifuso9.wav"))
    
    return prueba1, prueba2, prueba3
