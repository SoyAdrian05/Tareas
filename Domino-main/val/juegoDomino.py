
import random
import numpy as np
import os
import time
import pedirFichas as pf

# Matriz de las fichas del juego
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


fichas_bot=np.zeros((7,2))
fichas_jugador=np.zeros((7,2))
turno=0



def tomarFichas():
    ficha = pf.pedirImagen()
    return ficha

def darFichasJugador1():
    a = 0
    while a < 7:
        ficha = pf.pedirImagen()
        fichas_jugador[a] = fichas[ficha]
        del fichas[ficha]
        a += 1
def darFichasBot1():
    a = 0
    while a < 7:
        ficha = pf.pedirImagen()
        fichas_bot[a] = ficha
        del fichas[ficha]
        a += 1


#esto es temporal para ver si sirve el juego
#Se toma una ficha al azar
def tomar_ficha():
    val3 = random.randint(0,len(fichas)-1)
    ficha_tomada = fichas[val3]
    del fichas[val3]
    return ficha_tomada     
     
def darFichasJugador():
    a=0
    while a <7:
        val1 = random.randint(0,len(fichas)-1)
        fichas_jugador[a] = fichas[val1]
        del fichas[val1]
        a += 1
    
def darFichasBot():
    a=0
    while a<7:
        val2 = random.randint(0,len(fichas)-1)
        fichas_bot[a] = fichas[val2]
        del fichas[val2]
        a += 1
#-----------------------------------------------
def reseteo():
    print("\n"*10)
#Se debe volver a crear esto para la camara
def inicio():
    while True: 
        try: 
            print(chr(27)+"[1;37m"+" ")
            print("Bienvenido al Domino, elige el orden para recibir las fichas. \n"
                  "Si quieres empezar con tu mano, escribe 1. \n"
                  "Si quieres que el boto compience con fichas, escribe 2. \n"
                  "Si quieres que sea al azar escriba 3")
            while True: 
                try:
                    val = int(input("---> "))
                    if val == 1:
                        darFichasJugador1()
                        imprimir_fichas_jugador()
                        darFichasBot()
                        print("El bot ya tiene fichas")
                        break
                    elif val ==2:
                        darFichasBot()
                        print("El bot ya tiene fichas")
                        darFichasJugador()
                        imprimir_fichas_jugador()
                        break
                    elif val ==3:
                        val=random.randint(1,2)
                        if val==1:
                            darFichasJugador()
                            imprimir_fichas_jugador()
                            darFichasBot()
                            print("El bot ya tiene fichas")
                            break
                        elif val==2:
                            darFichasBot()
                            print("El bot ya tiene fichas")
                            darFichasJugador()
                            imprimir_fichas_jugador()
                            break
                except ValueError:
                    print("Por favor inserta un valor permitido")         
            #print("esta")
            break
        except KeyboardInterrupt:
            print("\nSe ha detenido el juego")
            break

def gana_mulas_compu(fichas2):
    n=0
    for i in range(len(fichas2)):
        if fichas2[i,0]==fichas2[i,1]:
            n +=1
            if n==4:
                print("Ha ganado el bot por tener 4 mulas o mas")
                return True
    return False
    

def gana_mulas_jugador(fichas2):
    print("Cuantas mulas tienes?")
    p=0
    n=0
    while p==0:
        try:
            val_mula = int(input("---> "))
            if val_mula>=4:
                for i in range(len(fichas2)):
                    if fichas2[i,0]==fichas2[i,1]:
                        n+=1
                if n>=4:
                    print("Ha ganado el jugador por tener 4 mulas o mas")
                else:
                    print("No tienes 4 mulas, mentiroso")
            p=val_mula
            return p
        except ValueError:
            print("Por favor inserta un valor permitido") 
            break

def tablero_juego(izq,der):
    global tablero
    tablero=[izq,der]
    imprimir_tablero_juego()

def imprimir_tablero_juego():
    print("El tablero es:")
    print("["+"{:.0f}".format(tablero[0])+","+"{:.0f}".format(tablero[1])+"]")
    
def Mula():
    turno_in=4
    while turno_in==4: 
        try:
            while turno_in==4: 
                try:
                    for i in range(6,-1,-1):
                        reseteo()
                        print("Jugador tienes la mula del %s? \n" %(i))
                        print("1--Si \n"
                              "2--No")
                        imprimir_fichas_jugador()
                        val3 = int(input("---> "))
                        if val3 == 1:
                            for j in range(len(fichas_jugador)):
                                if fichas_jugador[j,0]==i and fichas_jugador[j,1]==i:
                                    tablero_juego(i,i)
                                    fichas_jugador[j]=[9,9]
                                    imprimir_fichas_jugador()
                                    turno_in=1
                                    return True
                        val3=2
                        if val3 == 2:
                            for j in range(len(fichas_bot)):
                                if fichas_bot[j,0]==i and fichas_bot[j,1]==i:
                                    print("El bot tiene la mula del %s" %(i))
                                    tablero_juego(i,i)
                                    fichas_bot[j]=[9,9]
                                    turno_in=0
                                    return False
                    
                    if turno_in == 4:
                        reseteo()
                        imprimir_tablero_juego()
                        print("Jugador da una ficha")
                        val3 = int(input("---> "))
                        tablero_juego(fichas_jugador[val3,0], fichas_jugador[val3,1])
                        fichas_jugador[val3]=[9,9]
                        turno_in=1
                        return True
                    reseteo()
                except ValueError:
                    #print("Por favor inserta un valor permitido")
                    print("\n")
                    break
        except KeyboardInterrupt:
            print("\nSe ha detenido el juego")
            break

def Mula2():
    for j in range(len(fichas_bot)):
        if fichas_bot[j,0]==i and fichas_bot[j,1]==i:
            print("El bot tiene la mula del %s" %(i))
            tablero_juego(i,i)
            fichas_bot[j]=[9,9]
            return False
    
    num= random.randint(0,len(fichas_bot)-1)
    tablero_juego(fichas_bot[num,0], fichas_bot[num,1])
    fichas_bot[num]=[9,9]
    return False

def juego_domino(x):
    x = np.bitwise_not(x)
    turno2=x
    gana_compu=False
    gana_jugador=False
    pierde_jugador=False
    pierde_compu=False
    fin=False
    reseteo()
    imprimir_tablero_juego()
    while gana_jugador==False or gana_compu==False or pierde_jugador==False or pierde_compu==False: 
        try:
            while gana_jugador==False or gana_compu==False or pierde_jugador==False or pierde_compu==False: 
                try:
                    fin=empate()
                    if fin==True:
                        print("El juego acaba en empate")
                        return True
                    
                    if turno2==True and len(fichas)!=0:
                        print ("¿Quieres pedir una ficha?")
                        print("1) Si \n 2) No")
                        imprimir_fichas_jugador()
                        val5 = int(input("---> "))
                        if val5==1:
                            tomar=True
                            while tomar==True:
                                pierde_jugador=tomar_ficha_jugador()
                                if pierde_jugador==True:
                                    print(chr(27)+"[1;35m"+"Pierde el jugador por exceso de fichas")
                                    return True
                                
                                reseteo()
                                imprimir_tablero_juego()
                                print ("¿Quieres pedir una ficha?")
                                print("1) Si \n2) No")
                                imprimir_fichas_jugador()
                                val6 = int(input("---> "))
                                if val6==1:
                                    tomar=True
                                else:
                                    tomar=False
                        reseteo()
                        imprimir_tablero_juego()
                        print("¿Que ficha vas a tirar? (de 1 a 7)")
                        imprimir_fichas_jugador()
                        val4 = int(input("---> "))
                        if val4-1<=6 and val4-1>=0:
                            val4=val4-1
                            pierde_jugador=jugada(fichas_jugador,val4)
                            turno2= False
                            if pierde_jugador==True:
                                return True
                        else:
                            print("Ingrese un valor permitido")
                            #pierde_jugador=True
                            print(chr(27)+"[1;35m"+"Pierde el jugador por no colocar una ficha")
                            return True
                            
                        gana_jugador=gana(fichas_jugador,turno2)
                        if gana_jugador==True:
                            return True
                        reseteo()
                    else:
                        print("Turno compu")
                        a=jugada_compu()        #Si el bot tira ficha a=1, si no tira a=2
                        if a==1:
                            gana_compu=gana(fichas_bot,turno)
                            turno2= True
                            if gana_compu==True:
                                return True
                        
                        #Si el bot no tiro ficha
                        if a==2 and len(fichas)!=0:
                            pierde_compu=compu_pide_ficha()
                            turno2=True
                            if pierde_compu==True:
                                return True
                    
                except ValueError:
                    #print("Por favor inserta un valor permitido")
                    print("\n")
                    break
        except KeyboardInterrupt:
            print("\nSe ha detenido el juego")
            break

def jugada(fichas3,num):
    izq = tablero[0]
    der = tablero[1]
    if fichas3[num,0]!=9 and fichas3[num,1]!=9:
        if fichas3[num,0] == izq:
            izq = fichas3[num,1]
            fichas_jugador[num]=[9,9]
        elif fichas3[num,1] == izq:
            izq = fichas3[num,0]
            fichas_jugador[num]=[9,9]
        elif fichas3[num,0] == der:
            der = fichas3[num,1]
            fichas_jugador[num]=[9,9]
        elif fichas3[num,1] == der:
            der = fichas3[num,0]
            fichas_jugador[num]=[9,9]
        else:
            print("No puedes colocar esta ficha")
            print(chr(27)+"[1;35m"+"Pierdes por colocar una ficha que no se puede")
            return True
    tablero_juego(izq, der)

def tomar_ficha_jugador():
    if len(fichas)==0:
        print("Ya no hay fichas para comer")
        return False
    ficha_dada=False
    for i in range(len(fichas_jugador)):
        if fichas_jugador[i,0]==9:
            iz,d=tomar_ficha()
            fichas_jugador[i]=[iz,d]
            ficha_dada=True
            break
    if ficha_dada==False:
        return True
    else:
        return False

def imprimir_fichas_jugador():
    print("Tus fichas son:")
    for i in range(len(fichas_jugador)):
        if fichas_jugador[i,0]!=9:
            #print("%s) [%s,%s]" %(i+1,fichas_jugador[i,0],fichas_jugador[i,1]))
            print("%s)  ["%(i+1) +"{:.0f}".format(fichas_jugador[i,0])+",""{:.0f}".format(fichas_jugador[i,1])+"]")

def jugada_compu():
    izq = tablero[0]
    der = tablero[1]
    b=1
    for j in range(len(fichas_bot)):
        if fichas_bot[j,0]==izq and fichas_bot[j,1]==izq:
            tablero_juego(i,i)
            fichas_bot[j]=[9,9]
            return b
        elif fichas_bot[j,0]==der and fichas_bot[j,1]==der:
            tablero_juego(i,i)
            fichas_bot[j]=[9,9]
            return b
    
    for num in range(len(fichas_bot)):
        if fichas_bot[num,0] == izq:
            izq = fichas_bot[num,1]
            fichas_bot[num]=[9,9]
            tablero_juego(izq, der)
            return b
        elif fichas_bot[num,1] == izq:
            izq = fichas_bot[num,0]
            fichas_bot[num]=[9,9]
            tablero_juego(izq, der)
            return b
        elif fichas_bot[num,0] == der:
            der = fichas_bot[num,1]
            fichas_bot[num]=[9,9]
            tablero_juego(izq, der)
            return b
        elif fichas_bot[num,1] == der:
            der = fichas_bot[num,0]
            fichas_bot[num]=[9,9]
            tablero_juego(izq, der)
            return b
    b=2
    return b

def compu_pide_ficha():
    b=0
    #Vemos si el bot puede tomar una ficha
    for i in range(len(fichas_bot)):
        if fichas_bot[i,0]==9:
            iz,d=tomar_ficha()
            fichas_bot[i]=[iz,d]
            print(chr(27)+"[1;31m"+"El bot comio una ficha")
            print(chr(27)+"[1;37m"+"0")
            b=jugada_compu2(i)
            if b == 1:
                return False
    
    for i in range(len(fichas_bot)):
        if fichas_bot[i,0]!=9:
            b=b+1
            if b == 7:
                print("El bot tiene 7 fichas y no puede tirar ninguna ")
                print(chr(27)+"[1;35m"+"Pierde el bot")
                return True

def jugada_compu2(num):
    izq = tablero[0]
    der = tablero[1]
    if fichas_bot[num,0] == izq:
        izq = fichas_bot[num,1]
        fichas_bot[num]=[9,9]
        tablero_juego(izq, der)
        return 1
    elif fichas_bot[num,1] == izq:
        izq = fichas_bot[num,0]
        fichas_bot[num]=[9,9]
        tablero_juego(izq, der)
        return 1
    elif fichas_bot[num,0] == der:
        der = fichas_bot[num,1]
        fichas_bot[num]=[9,9]
        tablero_juego(izq, der)
        return 1
    elif fichas_bot[num,1] == der:
        der = fichas_bot[num,0]
        fichas_bot[num]=[9,9]
        tablero_juego(izq, der)
        return 1
    return 2
                

def gana(fichas4,turno3):
    n=0
    for i in range(len(fichas4)):
        if fichas4[i,0]==9:
            n=n+1
    if n==len(fichas4) and turno3 == False:
        print(chr(27)+"[1;36m"+"Gana el jugador")
        return True
    elif n==len(fichas4) and turno3 == True:
        print(chr(27)+"[1;36m"+"Gana el Bot")
        return True

def empate():
    if len(fichas)==0:
        izq = tablero[0]
        der = tablero[1]
        tirada_bot=0
        for i in range(len(fichas_bot)):
            if fichas_bot[i,0] == izq:
                tirada_bot=1
            elif fichas_bot[i,1] == izq:
                tirada_bot=1
            elif fichas_bot[i,0] == der:
                tirada_bot=1
            elif fichas_bot[i,1] == der:
                tirada_bot=1
        
        if tirada_bot==0:
            print("El bot no puede tirar ficha")
            print("¿Tu puedes tirar una ficha?")
            print("1) Si \n2) No")
            val6 = int(input("---> "))
            if val6==2:
                return True
        return False       
        

def pierde(turno3):
    if turno3==True:
        print(chr(27)+"[1;35m"+"Pierde el jugador por colocar una ficha que no va")
    elif turno3==False:
        print(chr(27)+"[1;35m"+"Pierde el bot por colocar una ficha que no va")

# Menu---------------
#Turno = 1 jugador, Turno = 2 bot
def Menu():
    global fin_juego
    fin_juego=False
    inicio()
    num_mulas=gana_mulas_jugador(fichas_jugador)
    fin_juego=gana_mulas_compu(fichas_bot)
    if fin_juego==False:
        if num_mulas==0:
            turno=Mula2()
        else:
            turno=Mula()
        fin_juego=juego_domino(turno)

    if fin_juego==True:
        print("El juego termino")
    else:
        print("Ocurrio un problema")

Menu()

