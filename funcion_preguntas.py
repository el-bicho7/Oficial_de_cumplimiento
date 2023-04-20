#!/usr/bin/env python
import random
import os
import textwrap
from time import sleep

'''Funcion para encontrar las respuestas, basandose si las respuestas son en base a un str o en un diccionario.'''

def preguntas_str(diccionario, tema, pregunta):
    '''Diccionario de str -> str'''

    cont = True
    calificacion = 0
    while cont == True:
        score = 0
        error = 0
        incorrectas = {}
        print(tema.center(70, "-"))
        n = int(input("Cuantas preguntas? (max "+ str(len(diccionario)) +")\n\t"))      # numero de preguntas
        l = random.sample(list(diccionario.keys()) , n)          #lista de persona a preguntar
        os.system('cls')
        for i in l:                                         #iteraccion de la lista
            print(tema.center(70, "-"))
            print("\tScore: ", score, "\tErrores: ", error)
            resp = input(pregunta + i + "?\t\n\t").lower()  #Recibe la respuesta y la hace minusculas
            if resp == diccionario[i].lower():              #Revisa la respuesta recibida y nos indica si es correcto o incorrecto.
                score += 1
                print("\tCorrecto")
                sleep(1)
                os.system('cls')
            else:
                error +=1
                print("\tIncorrecto\tRespuesta:\t" + diccionario[i])
                incorrectas[i] = diccionario[i]
                sleep(3)
                os.system('cls')

        calificacion = round((score/n*100), 2)                  #Obtiene la calificacion
        print("".center(70, "-"))
        if len(incorrectas) > 0:
            print("Respuestas incorrectas")                         #Imprime las respuestas incorrectas si hay respuestas incorrectas
            for i in incorrectas:
                print(i,"\t-\t", incorrectas[i])
        print("Calificacion:\n\t", calificacion,"%")
        cont = input("Intentar otra vez (s/n)\n\t")
        if cont == 's':
            os.system('cls')
            cont = True
        else:
            os.system('cls')
            cont = False
    return calificacion

def preguntas_list(diccionario, tema, pregunta):
    '''Diccionario str -> list'''

    caificacion = 0
    attempts = 3
    score = 0
    n = 0                                                   #Contador de intentos
    dic, lst = random.choice(list(diccionario.items()))     #Elegir un diccionario para preguntar y su lista de respuestas
    response = []                                           #Crear la lista para agregar los resultados
    lst = list(map(lambda z: z.casefold(),lst))             #Hace minusculas todos los objetos de la lista de aciertos
    pregunta = pregunta + dic + ": (singular)"
    wrapp = textwrap.fill(pregunta)
    while (attempts >0 and len(lst)>0):

        print(tema.center(70, "-"))
        print("\tScore: ", score, "\tFaltan: ", len(lst), "\tIntentos restantes: ", attempts)
        print(wrapp)
        resp = input("\t").lower() #Captura la respuesta
        if resp not in response:                                #Revisa que aun no se encuentre la respuesta en la lista
            if resp in lst:                                     #Respuesta en la lista de aciertos
                    inde = lst.index(resp)                      #Encontrar el lugar donde esta la respuesta en la lista de respuestas
                    response.append(lst.pop(inde))              #Extrae la respuesta y la coloca en una variable de respuestas
                    score += 1                                  #Suma un acierto
                    n +=1                                       #Cuenta los intentos
                    print("\tCorrecto")
                    sleep(1)
                    os.system('cls')
                    continue
            else:
                attempts -= 1                                   #Resta los intentos
                n +=1
                print("\tIncorrecto")
                sleep(2)
                os.system('cls')
                if attempts == 0:
                    break
        else:
            print("Respuesta repetida")
            sleep(1)
            os.system('cls')
    calificacion = round((score/n*100), 2)
    print("".ljust(70, "="))
    print("Te faltaron:")
    for z in lst:
        print("\t" + z.upper())

    print("Calificacion:\n\t", calificacion, "%")
    cont = input("Intentar otra vez (s/n)\n\t")
    if cont == 's':
        os.system('cls')
        cont = True
    else:
        os.system('cls')
        cont = False
    return calificacion
