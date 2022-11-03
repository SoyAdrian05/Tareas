# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 03:14:26 2022

@author: Adrian
"""

import numpy as np

def parametros():
    P = np.zeros((30,3))
    T = np.zeros((30,2))
    b = np.zeros(2)
    w = np.zeros((2,3))
    return P, T, b, w

def targets(T):
    for i in range(30):
        if i<10:
            T[i] = [-1,-1]
        elif i>9 and i<20:
            T[i] = [-1,1]
        else:
            T[i] = [1,1]
    return T

def entrenamiento(P,T,alpha,epocas):
    b = np.zeros(2)
    w = np.zeros((2,3))
    for i in range(epocas):
        for j in range(len(P)):
            a = np.dot(w,P[j]) + b
            e = T[j] - a
            w = w + alpha*np.outer(e,P[j])
            b = b + alpha*e
    return w, b
    
def alphaCalculo(P):
    R=0
    for i in range(len(P)):
        R=R+0.25*np.outer(P[i],np.transpose(P[i]))
    eigenvalor,vector=np.linalg.eig(R)
    landamax=max(eigenvalor)
    alpha=1/(4*landamax)*0.99
    return alpha

def eficacia(P,T,alpha,b,w):
    erroneos = 0
    for j in range(len(P)):
        error = np.dot(w,P[j]) + b
        error = np.where(error < 0,-1,1)
        error = T[j] - error
        w = w + np.outer(error,P[j])
        b = b + error
        
        if (error[0] != 0 or error[1] != 0):
            erroneos = erroneos + 1

    eficiencia = (30 - erroneos)*100/len(P)
    return eficiencia, erroneos