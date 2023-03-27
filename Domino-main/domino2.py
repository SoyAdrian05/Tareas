# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 18:23:34 2023

@author: yessi
"""

from skimage import io,measure,color
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import math
plt.close('all')

imagen1=io.imread('fM4.jpeg')
gris=color.rgb2gray(imagen1)
binario1=(gris<0.5).astype(np.int)

# plt.figure()
# plt.imshow(imagen1)
Ima9,Can9=measure.label(binario1,return_num=True,connectivity=2)
# plt.imshow(Ima9)
columnas=binario1.shape[0]/2
#imagen2=columnas[-1]

r2=measure.regionprops(Ima9)
fig, ax = plt.subplots()
ax.imshow(Ima9, cmap=plt.cm.gray)
for props in r2:
    y0, x0 = props.centroid
    orientation = props.orientation
    x1 = x0 + math.cos(orientation) * 0.5 * props.axis_minor_length
    y1 = y0 - math.sin(orientation) * 0.5 * props.axis_minor_length
    
    ax.plot((x0, x1), (y0, y1), '-r', linewidth=2.5)
    ax.plot(x0, y0, '.g', markersize=15)

    minr, minc, maxr, maxc = props.bbox
    bx = (minc, maxc, maxc, minc, minc)
    by = (minr, minr, maxr, maxr, minr)
    ax.plot(bx, by, '-b', linewidth=2.5)

plt.show()



imagen=io.imread('fM1.jpeg')
gris=color.rgb2gray(imagen)
binario=(gris<0.5).astype(np.int)

# plt.figure()
# plt.imshow(imagen1)
Ima4,Can4=measure.label(binario,return_num=True,connectivity=2)
# plt.imshow(Ima9)


r=measure.regionprops(Ima4)
fig, ax = plt.subplots()
ax.imshow(Ima4, cmap=plt.cm.gray)
for props in r:
    y0, x0 = props.centroid
    orientation = props.orientation
    x1 = x0 + math.cos(orientation) * 0.5 * props.axis_minor_length
    y1 = y0 - math.sin(orientation) * 0.5 * props.axis_minor_length
    
    ax.plot((x0, x1), (y0, y1), '-r', linewidth=2.5)
    ax.plot(x0, y0, '.g', markersize=15)

    minr, minc, maxr, maxc = props.bbox
    bx = (minc, maxc, maxc, minc, minc)
    by = (minr, minr, maxr, maxr, minr)
    ax.plot(bx, by, '-b', linewidth=2.5)


plt.show()

