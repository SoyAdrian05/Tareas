# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:29:31 2023

@author: yessi
"""

from skimage import io, measure
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

print('Primera parte del programa: Entrenamiento')
bin6 = (io.imread('entrena6.bmp')>100).astype(np.int16)
bin9 = (io.imread('entrena9.bmp')>100).astype(np.int16)
plt.close('all')
plt.figure()
plt.imshow(bin6)
# plt.figure()
# plt.imshow(bin9, cmap = 'gray')
#plt.pause(0.1)
ima6, can6 = measure.label(bin6,return_num=True, connectivity = 2) 
# can 6 regresa el numero de objetos encontrados
# conectividad 1 - pregunta x 4 vecinos, conectividad 2 - pregunta x 8 vecinos 
ima9, can9 = measure.label(bin9,return_num=True, connectivity = 2)
plt.figure()
plt.imshow(ima6, cmap = 'gray')
# # plt.figure()
# # plt.imshow(ima9, cmap = 'gray')
#ima6 = np.where(ima6 == 1,3,0) #busca 3, si es -> 1 si no es -> 0

for i in range(1,3,1): #empieza 1 y pasa a 2 (llega max-1)
    if(i==1):
         numero = ima6
         cantidad = can6
         print('Se procesa el número 6')
    else:
        numero = ima9
        cantidad = can9
        print('Se procesa el número 9')
    dato =[]
    for j in range(1,cantidad,1):
        print('objeto %s de %s' %(j,cantidad))
        s1 = np.where(numero == j,1,0) #INICIA CLASIFICADOR
        #plt.figure()
        #plt.imshow(s1)
        s2 = ndimage.binary_fill_holes(s1).astype(np.int16)
        s3 = np.logical_xor(s1,s2) 
        plt.figure()
        plt.imshow(s3)
        Fil1, Col1 = np.nonzero(s1)
        Fil2, Col2 = np.nonzero(s3)
        NFmin = min(Fil1) #min y max filas y columnas
        NFmax = max(Fil1)
        NCmin = min(Col1)
        NCmax = max(Col1)
        bolitamin = min(Fil2) 
        bolitamax = max(Fil2)
        medio = (bolitamax-bolitamin)/2.0 + bolitamin
        dato.append((medio-NFmin)/(NFmax-NFmin))
        
    if(i==1):
        dato6 = dato
    else:
        dato9 = dato
        
# plt.figure()
# plt.imshow(s3, cmap='gray')
    
# plt.figure()
# plt.hist(dato9,bins='auto',alpha=0.75,rwidth=0.3,color='r',label='numero 9')
# plt.hist(dato6,bins='auto',alpha=0.75,rwidth=0.3,color='g',label='numero 6')
# plt.legend(loc='upper right')

# #Inicia segunda parte
# umbral = 0.5
# print('Segunda parte del programa: Entrenamiento')
# prueba = (io.imread('prueba69.bmp')>100).astype(np.int16)
# plt.figure()
# plt.imshow(prueba, cmap = 'gray')
# ima, can = measure.label(prueba,return_num=True, connectivity = 2) 
# numero6 = np.zeros_like(prueba)
# numero9 = np.zeros_like(prueba)
# plt.figure()
# plt.imshow(np.block([[numero6],[numero9]])) #hace un bloque de dos mas pequeños

# for j in range(1,can,1):
#     print('objeto %s de %s' %(j,can))
#     s1 = np.where(ima == j,1,0) 
#     s2 = ndimage.binary_fill_holes(s1).astype(np.int16)
#     s3 = np.logical_xor(s1,s2) #parte rellena
#     Fil1, Col1 = np.nonzero(s1)
#     Fil2, Col2 = np.nonzero(s3)
#     if len(Fil2) == 0: #ruido/basura
#         continue
#     bolitamin = min(Fil2) 
#     bolitamax = max(Fil2)
#     NFmin = min(Fil1) #min y max filas y columnas
#     NFmax = max(Fil1)
#     NCmin = min(Col1)
#     NCmax = max(Col1)
#     medio = (bolitamax-bolitamin)/2.0 + bolitamin
#     dato.append((medio-NFmin)/(NFmax-NFmin))
#     if dato[-1] > umbral:
#         print('6')
#         numero6[Fil1,Col1] = 1
#         plt.imshow(np.block([[numero6],[numero9]])) #hace un bloque de dos mas pequeños
#         plt.pause(1)
#     else:
#         print('9')
#         numero9[Fil1,Col1] = 1
#         plt.imshow(np.block([[numero6],[numero9]])) #hace un bloque de dos mas pequeños
#         plt.pause(1)
            

            













