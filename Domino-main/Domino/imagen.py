
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:17:49 2023
@author: adria
"""

# normalizar imagen7

from skimage import data, io, color, measure
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 
from scipy import ndimage

#os.chdir('D:/Adrian/Escuela/Reconocimiento de Patrones/Domino-main/')


plt.close('all')
def imageRecognition(file_name):
    # imagen_orin = io.imread(file_name)
    imagen = cv2.imread(file_name)
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    otsu_threshold, image_result = cv2.threshold(gray, 75, 255,cv2.THRESH_BINARY_INV) #100
    cv2.imshow('imagen',image_result)
    return image_result



def pedirImagen():
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        cv2.imshow('video', frame)
        
        
        #print(gray)
        if cv2.waitKey(1) == ord('p'):
            out = cv2.imwrite('captura.jpg', frame)
            break
    video.release()
    cv2.destroyAllWindows()
    imagen = imageRecognition('captura.jpg')
    return imagen

#imagen = pedirImagen()
imagen = io.imread('captura.jpg')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
otsu_threshold, image_result = cv2.threshold(gray, 75, 255,cv2.THRESH_BINARY)
ima_recor = image_result[100:450,160:560] 
# plt.figure()
# plt.imshow(ima_recor, cmap = 'gray')
#ima = ndimage.binary_fill_holes(ima_recor).astype(int)
#plt.figure()
#plt.imshow(ima, cmap = 'gray')
ima, num = measure.label(ima_recor, return_num = True, connectivity = 2)
ima = np.where(ima == 0,1,0)
s2 = np.where(ima == 1, 0, 1)

plt.figure()
plt.imshow(s2, cmap = 'gray')
s3 = np.logical_xor(ima,s2) 
plt.figure()
plt.imshow(s3)


a = 0
Fil1, Col1 = np.nonzero(ima)
Fil2, Col2 = np.nonzero(s3)
NFmin = min(Fil1) #min y max filas y columnas
NFmax = max(Fil1)
NCmin = min(Col1)
NCmax = max(Col1)
bolitamin = min(Fil2) 
bolitamax = max(Fil2)
#cv2.imshow('imagen', ima_recor)
# plt.figure()
# plt.imshow(ima_recor, cmap = 'gray')
