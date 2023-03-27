# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:35:21 2023

@author: diana
"""

from skimage import io,measure,color
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
plt.close('all')

imagen1=io.imread('d1_2.jpg')
gris=color.rgb2gray(imagen1)
binario1=(gris<0.5).astype(np.int16)
recorte1=binario1[0:370,:]

contorno=measure.find_contours(recorte1)
for contour in contorno:
    plt.plot(contour[:, 1], contour[:, 0], linewidth=2)

recorte2=binario1[410:800,:]
contorno2=measure.find_contours(recorte2)
for contour in contorno2:
    plt.plot(contour[:, 1], contour[:, 0], linewidth=2)


# plt.figure()
# plt.imshow(imagen1)
# Ima9,Can9=measure.label(binario1,return_num=True,connectivity=2)
# plt.figure()
# plt.imshow(Ima9)
# recorte1=Ima9[0:370,:]
# plt.figure()
# plt.imshow(recorte1,cmap='gray')
# recorte2=Ima9[410:800,:]
# plt.figure()
# plt.imshow(recorte2,cmap='gray')



# r2=measure.regionprops(recorte1)
# fig, ax = plt.subplots()
# ax.imshow(recorte1, cmap=plt.cm.gray)
# m=0
# for props in r2:
#     y0, x0 = props.centroid
#     orientation = props.orientation
#     x1 = x0 + math.cos(orientation) * 0.5 * props.axis_minor_length
#     y1 = y0 - math.sin(orientation) * 0.5 * props.axis_minor_length
    
#     ax.plot((x0, x1), (y0, y1), '-r', linewidth=2.5)
#     ax.plot(x0, y0, '.g', markersize=15)

#     minr, minc, maxr, maxc = props.bbox
#     bx = (minc, maxc, maxc, minc, minc)
#     by = (minr, minr, maxr, maxr, minr)
#     ax.plot(bx, by, '-b', linewidth=2.5)
#     m=m+1
# plt.show()
# m
