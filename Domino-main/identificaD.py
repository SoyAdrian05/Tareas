# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:08:50 2023

@author: yessi
"""



import cv2

from skimage import io,data,color
import numpy as np
import matplotlib.pyplot as plt
# from sklearn import datasets
# import mpl_toolkits.mplot3d
plt.close('all')#quitar ventanas

img = cv2.imread('numero5RMY.bmp')
kernel = np.ones((7,7),np.uint8)
dilatacion = cv2.dilate(img,kernel,iterations = 1)

i=cv2.imread('D6.1.jpeg')
plt.figure()
plt.imshow(i)

