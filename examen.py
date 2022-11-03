# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 18:25:49 2022

@author: Adrian
"""
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.proj3d import proj_transform
from matplotlib.patches import FancyArrowPatch
import numpy as np
import matplotlib.pyplot as plt
import vectores_audio as vec_aud
import RedNeuronal as rn

P = np.zeros((30,3))
T = np.zeros((30,2))


class Arrow3D(FancyArrowPatch):

    def __init__(self, x, y, z, dx, dy, dz, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._xyz = (x, y, z)
        self._dxdydz = (dx, dy, dz)

    def draw(self, renderer):
        x1, y1, z1 = self._xyz
        dx, dy, dz = self._dxdydz
        x2, y2, z2 = (x1 + dx, y1 + dy, z1 + dz)

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        super().draw(renderer)
        
    def do_3d_projection(self, renderer=None):
        x1, y1, z1 = self._xyz
        dx, dy, dz = self._dxdydz
        x2, y2, z2 = (x1 + dx, y1 + dy, z1 + dz)

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))

        return np.min(zs) 
    
def _arrow3D(ax, x, y, z, dx, dy, dz, *args, **kwargs):
    '''Add an 3d arrow to an `Axes3D` instance.'''

    arrow = Arrow3D(x, y, z, dx, dy, dz, *args, **kwargs)
    ax.add_artist(arrow)

setattr(Axes3D, 'arrow3D', _arrow3D)


def plano3d(intx,inty, intz):
    puntos = [[ float(intx), 0 , 0 ],[ 0 ,  float(inty), 0],[ 0 , 0 , float(intz)]]
    punto0,punto1,punto2 = puntos 
    
    Ax,Ay,Az = punto0
    Bx,By,Bz = punto1
    Cx,Cy,Cz = punto2
    
    ABx,ABy,ABz = [Bx-Ax,By-Ay,Bz-Az]
    ACx,ACy,ACz = [Cx-Ax,Cy-Ay,Cz-Az]
    ABcruzAC = [ABy*ACz - ABz*ACy,ABz*ACx - ABx*ACz,ABx*ACy - ABy*ACx]
    
    punto = np.array(punto0)
    vectorNormal = np.array(ABcruzAC) 
    d = -punto.dot(vectorNormal)
    
    xx,yy = np.meshgrid(range(-15, 5),range(-15,5))
    z = (-vectorNormal[0]*xx - vectorNormal[1]*yy-d)*1./vectorNormal[2]
    return xx,yy,z

def entropia(datos):
    H = 0
    for i in range(len(datos[:500])):
        H += datos[i]*np.log(1/datos[i])/1e9
        
    H1 = 0
    for i in range(500,len(datos[:1000])):
        H1 += datos[i]*np.log(1/datos[i])/1e9
        
    H2 = 0
    for i in range(1000,len(datos[:2500])):
        H2 += datos[i]*np.log(1/datos[i])/1e9
    return[H,H1,H2]

palabra1 = vec_aud.audiosPalabra1()
palabra2 = vec_aud.audiosPalabra2()
palabra3 = vec_aud.audiosPalabra3()


for i in range(10):
    P[i] = entropia(palabra1[i])
    P[i+10] = entropia(palabra2[i])
    P[i+20] = entropia(palabra3[i])    

T = rn.targets(T)

alpha = rn.alphaCalculo(P)
w, b = rn.entrenamiento(P, T,alpha, 500)

print(w)
intx1 =-b[1]/w[0,0] 
inty1 =-b[1]/w[0,1] 
intz1 =-b[1]/w[0,2] 

intx2 =-b[0]/w[1,0] 
inty2 =-b[0]/w[1,1] 
intz2 =-b[0]/w[1,2] 

xx1,yy1,z1 = plano3d(intx1,inty1,intz1)
xx2,yy2,z2 = plano3d(intx2,inty2,intz2)

plt3d=plt.figure().gca(projection='3d')
plt3d.plot_surface(xx1,yy1,z1,alpha=0.8,color='yellow')
plt3d.plot_surface(xx2,yy2,z2, alpha=0.8,color='orange')
plt.show()

for i in range(10):
    plt3d.scatter(P[i][0],P[i][1],P[i][2], color = 'red')
    plt3d.scatter(P[i+10][0],P[i+10][1],P[i+10][2], color = 'green')
    plt3d.scatter(P[i+20][0],P[i+20][1],P[i+20][2], color = 'blue')


plt3d.arrow3D(-4.5,-3.5,0,intx1*5,inty1*10,intz1*5,mutation_scale = 10,fc = 'gold')

plt3d.arrow3D(-4.5,-3.5,0,intx2*10,inty2*5,intz2*5,mutation_scale = 10,fc='lightcoral')

eficiencia, erroneos = rn.eficacia(P, T, alpha, b, w)

print('Eficiencia: ',eficiencia,'%')
print('acertando en: ',30 - erroneos)
print('El peso es: ' ,w)
print('La polarización es: ', b)



