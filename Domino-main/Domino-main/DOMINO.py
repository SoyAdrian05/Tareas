# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:29:51 2023

@author: Adrian
"""
import random
import numpy as np 

fichas = ["00", "01", "02", "03", "04", "05", "06", "11", "12", "13", "14","15", "16", 
          "22","23","24", "25", "26", "33", "34", "35", "36", "44", "45", "46", "55", "56", "66"]

fichas_en_juego = fichas



num_fichas_juego = 7

mano_jugador1 = np.zeros(7)
mano_jugador2 = np.zeros(7)

mano_prueba = ["13", "33", "66", "42", "35", "56", "25"]


def elegirFicha():
    while True:
        try:
            num_ficha_jugador = int(input("Por favor selecciona una ficha: "))
            print("Tu ficha es: ", fichas[num_ficha_jugador-1])
            return num_ficha_jugador
            break
        except ValueError:
            print("No has ingresado un número")      
     
def rivalFicha():
    return random.randint(0, len(fichas)) - 1

def darFichasJugador():
    a = 0
    while a <7:
        #print(len(fichas_en_juego))
        val1 = random.randint(0,len(fichas_en_juego)-1)
        #print(fichas_en_juego,"\n")
        #print(val1, "\n")
        mano_jugador1[a] = fichas_en_juego[val1]
        del fichas_en_juego[val1]
        a += 1
    
def darFichasBot():
    a = 0
    while a<7:
        #print(len(fichas_en_juego))
        val2 = random.randint(0,len(fichas_en_juego)-1)
        #print(fichas_en_juego,"\n")
        mano_jugador2[a] = fichas_en_juego[val2]
        del fichas_en_juego[val2]
        a += 1
        
def inicio():
    while True: 
        try: 
            print("Bienvenido al Domino, elige el orden para recibir las fichas. \n"
                  "Si quieres empezar con tu mano, escribe 1. \n"
                  "Si quieres que el bot comience con fichas, escribe 2.")
            while True: 
                try:
                    val = int(input("---> "))
                    #Inicio de juego
                    if val == 1:
                        darFichasJugador()
                        darFichasBot()
                        print("Tus fichas son: \n", mano_jugador1 )
                        print("las fichas del bot son: \n", mano_jugador2 )

                        return mano_jugador1, mano_jugador2
                    else:
                        darFichasBot()
                        darFichasJugador()
                        print("Tus fichas son: \n", mano_jugador1 )
                        print("las fichas del bot son: \n", mano_jugador2 )
                        return mano_jugador1, mano_jugador2
                except ValueError:
                    print("Por favor inserta un valor permitido")         

            
            print()
            break
        except KeyboardInterrupt:
            print("\nSe ha detenido el juego")
            break

        
        
def mulas_del_bot(mano_bot):
    for i in range(0, len(mano_bot)):
        mano_bot[i] = int(mano_bot[i])
    mulas = [00, 11, 22, 33, 44, 55, 66]
    valor = -1
    x = sorted(mano_bot)
    for i in range(len(x)):
        for j in range(len(mulas)-1,0,-1):
            if x[i] == mulas[j]:
                if valor >=  x[i]:
                    valor = x[i]
                else: 
                    pass
    print("La mula mas grande fue: ", valor)
    return valor
                
        
def pedirFicha(mano_jugador):
    for i in range(0, len(mano_jugador)):
        mano_jugador[i] = int(mano_jugador[i])
    while True: 
        try:
            print("¿Que fichas seleccionas?")
            valor = int(input("---> "))
            for i in range(len(mano_jugador)):
                if valor == mano_jugador[i]:
                    print("Ficha valida, es ---> {}".format(mano_jugador[i]))
                    return  valor
                # else:
                #     print("Por favor ingresa una ficha valida")
        except ValueError:
            print("\nPor favor inserta un valor permitido\n")
    
    
#pedirFicha(mano_prueba)
# while Ture: 
#     try: 

    
# mano_bot = ["02","22","33","55","66","23","32"]
# mulas_del_bot(mano_bot)
mano_jugador, mano_bot = inicio()
while True: 
    try: 
        print("Comencemos el juego, para empezar. ¿Tienes la mula mas alta?")
        val = input("----> ")
        if val == "s":
            mula_usuario = pedirFicha(mano_jugador)
            mula_bot = mulas_del_bot(mano_bot)
            if mula_usuario > mula_bot: 
                print("El usuario tira primero")
            else: 
                print("El bot tira primero")
            
        elif val == "n":
            #mano_bot = ["12","21","32","34","55","34"]
            mula_usuario = pedirFicha(mano_jugador)
            mula_bot = mulas_del_bot(mano_bot)
            if mula_usuario > mula_bot: 
                print("El usuario tira primero")
            else: 
                print("El bot tira primero")
                        
        else:
            print("Por favor inserte un valor valido\n")
                                
    except ValueError: 
        print("Por favor inserta un valor permitido\n")   
   

    

     
 