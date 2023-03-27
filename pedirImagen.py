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

os.chdir('D:/Adrian/Escuela/Reconocimiento de Patrones/Domino-main/')


plt.close('all')
def imageRecognition(file_name):
    # imagen_orin = io.imread(file_name)
    imagen = cv2.imread(file_name)
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    otsu_threshold, image_result = cv2.threshold(gray, 100, 255,cv2.THRESH_BINARY)
    cv2.imshow('imagen',image_result)
    return image_result



def pedirImagen():
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        cv2.imshow('video', frame)
        
        
        #print(gray)
        if cv2.waitKey(1) == ord('q'):
            out = cv2.imwrite('captura.jpg', frame)
            break
    video.release()
    cv2.destroyAllWindows()
    imagen = imageRecognition('captura.jpg')
    return imagen

imagen = pedirImagen()

ima, num = measure.label(imagen, return_num = True, connectivity = 2)