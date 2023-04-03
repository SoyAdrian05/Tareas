# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 21:49:33 2023

@author: Adrian
"""

import numpy as np



matriz=np.zeros((7,7,2))
fichas =[]
for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i,j]=[i,j]
        if i==j:
            matriz[i,j]=[i,j]
            break
n=0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i,j,0]==0 and matriz[i,j,1]==0 and n==0:
            n=1
            fichas.append(matriz[i,j])
        elif matriz[i,j,0]!=0 or matriz[i,j,1]!=0:
            fichas.append(matriz[i,j])
a = [5,5]
print(type(a))
a = np.array(a)
print(type(a))

fichas_bot=np.zeros((7,2))
fichas_jugador=np.zeros((7,2))

# def darFichasJugador1():
#     a = 0
#     while a < 7:
#         ficha = [5,5]
#         fichas_jugador[a] = ficha
#         for i in range(fichas):
#             if fichas[]
#         a += 1
        
# darFichasJugador1()

for i in range(len(fichas)):
    print("\n---> {}".format(fichas[i]))
    # var = fichas[i] 
    # print(var)
    # print(type(fichas))
    
    # for j in range(len(var)):
    #     if var[ ==
        
    if fichas[i] == a:
        print("Aquí está")
        break