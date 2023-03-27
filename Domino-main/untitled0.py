# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:12:02 2023

@author: adria
"""
from skimage import data, io, color, measure
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 

os.chdir('D:/Adrian/Escuela/Reconocimiento de Patrones/Domino-main/')

video = cv2.VideoCapture(0)
a = 0

plt.close('all')
def imageRecognition(file_name):
    # imagen_orin = io.imread(file_name)
    imagen = cv2.imread(file_name)
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # # # imagen = cv2.GaussianBlur(imagen, (5,5), 0)
    # plt.figure()
    # plt.imshow(imagen_orin)
    # cv2.imshow('imagen', imagen)
    otsu_threshold, image_result = cv2.threshold(gray, 100, 255,cv2.THRESH_BINARY)
    # plt.figure()
    # plt.imshow(image_result)
    cv2.imshow('imagen',image_result)
    # # print("Obtained threshold: ", otsu_threshold)
    # cv2.imshow('image_result' , image_result)
    # plt.imshow(image_result,  cmap = 'gray')
    # gris = color.rgb2gray(imagen)
    # binario = (gris>0.5).astype(np.int)
    # plt.figure()
    # plt.imshow(binario, cmap = 'gray')
    
    # contorno=measure.find_contours(binario)
    # for contour in contorno:
    #     plt.plot(contour[:, 1], contour[:, 0], linewidth=2)

    # contorno2=measure.find_contours(binario)
    # for contour in contorno2:
    #     plt.plot(contour[:, 1], contour[:, 0], linewidth=2)


while True:
    
    ret, frame = video.read()
    
    cv2.imshow('video', frame)
    
    
    #print(gray)
    if cv2.waitKey(1) == ord('q'):
        out = cv2.imwrite('captura.jpg', frame)
        break
    

video.release()
cv2.destroyAllWindows()
imageRecognition('captura.jpg')
# imagen = io.imread('captura.jpg')
# imagen = cv2.imread('captura.jpg')
# otsu_threshold, image_result = cv2.threshold(imagen,100, 255,cv2.THRESH_BINARY)
# plt.figure()
# plt.imshow(imagen, cmap = 'gray')

# plt.figure()
# plt.imshow(image_result, cmap = 'gray')

