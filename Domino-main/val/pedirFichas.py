# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 14:58:01 2023

@author: Adrian
"""

from skimage import data, io, color, measure
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 
from scipy import ndimage



def calcularPos(imagen, pos):
    pun_maximo_enX = []
    pun_maximo_enY = []
    for i in range(imagen.shape[0]):
        prom = np.sum(imagen[i])
        pun_maximo_enX.append(prom)
    posX = np.argmax(pun_maximo_enX)
    
    for j in range(imagen.shape[1]):
        prom = np.sum(imagen[i])
        pun_maximo_enY.append(prom)
    posY = np.argmax(pun_maximo_enY)
    
    return posX

def imageRecognition(imagen,frame_x_ini, frame_y_ini,frame_x_fin, frame_y_fin ):
    imagen = cv2.imread(imagen)
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    otsu_threshold, image_result = cv2.threshold(gray, 100, 255,cv2.THRESH_BINARY_INV) #75 y 255
    imagen_recortada = image_result[frame_x_ini:frame_x_fin,frame_y_ini:frame_y_fin] 
    return imagen_recortada

def pedirImagen():
    frame_x_ini = 80
    frame_x_fin = 400
    frame_y_ini = 200
    frame_y_fin = 420
    
    
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        start_point = (frame_y_ini, frame_x_ini)
        end_point = (frame_y_fin, frame_x_fin)
        color = (255, 0, 0)
        thickness = 2
        cv2.rectangle(frame, start_point, end_point, color, thickness)
        cv2.imshow('video', frame)
        if cv2.waitKey(1) == ord('o'):
            out =cv2.imwrite('prueba.jpg', frame)
            break
        elif cv2.waitKey(1) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    
    imagen = imageRecognition('prueba.jpg', frame_x_ini, frame_y_ini, frame_x_fin, frame_y_fin)
    ima, num = measure.label(imagen, return_num = True, connectivity = 2)
    clas_ima = ima
    num_puntos_ima = [] # ---> Array de los puntos en imagen
    prom_puntos = [] # Promedio de cada punto 

    for j in range(1,num+1,1):
        s1 = np.where(clas_ima == j,1,0)
        s2 = ndimage.binary_fill_holes(s1).astype(np.int16)
        prom = np.sum(s2)
        # print(prom, "--> para la fig {}".format(j))
        if prom >500 and prom <3000:
            num_puntos_ima.append(s2)
            prom_puntos.append(prom)

    punto_medio_ima = num_puntos_ima[np.argmax(prom_puntos)]
    num_puntos_ima.pop(np.argmax(prom_puntos))
    pun_med = []
    
    for i in range(punto_medio_ima.shape[0]):
        prom = np.sum(punto_medio_ima[i])
        pun_med.append(prom)
        
    pos = np.argmax(pun_med)
    a = 0
    b = 0
    
    for n in range(len(num_puntos_ima)):
        puntito = num_puntos_ima[n]
        posX= calcularPos(puntito, pos)
        
        if posX < pos:
            a = a + 1 
        else:
            b = b + 1
    print("La ficha es de --> [{},{}]".format(a,b))
    ficha = np.array([a,b])
    print("ficha: ",ficha)
    return [a,b]
    

resultado = pedirImagen()