import random
import os
from time import sleep

'''Leyes relativas al SFM y DCG a SOB'''

def Leyes():
    calificacion = 0
    while True:
        print("---------------------------Leyes relativas al SFM y DCG a SOB---------------------------")
        leyes = { 1 : {"ley" : "LGOAAC", "art": "95Bis", "if" : ["Centro Cambiario", "Transmisor de Dinero", "SOFOM ENR"]},
                  2 : {"ley" : "LGOAAC", "art": "95", "if" : ["Almacen General de Depostio", "Casa de Cambio"]},
                  3 : {"ley" : "LGOAAC", "art": "95Bis 87D y LIC 115", "if" : "SOFOM ER"},
                  4 : {"ley" : "LSOCAP", "art": "71 y 72", "if" : "Sociedades Coop. de Ahorro y Prestamo"},
                  5 : {"ley" : "LITF", "art": "58", "if" : ["Intituciones de Financiamiento Colectivo", "Inst. de Fondo de Pago Colectivo"]},
                  6 : {"ley" : "LFNDARFP", "art": "60", "if" : "FNDARFP"},
                  7 : {"ley" : "LACP", "art": "124", "if" : ["SOFIPO", "SOFICO","OIF"]},
                  8 : {"ley" : "LIC", "art": "115", "if" : ["Inst. Banca Multiple", "Inst. Banca Desarrollo"]},
                  9 : {"ley" : "LFI", "art": "91", "if" : "Sociedades Anonimas de Fondo de Inversion"},
                  10 : {"ley" : "LMV", "art": "212", "if" : "Casa de Bolsa"},
                  11 : {"ley" : "LMV", "art": "226", "if" : "Asesores de Inversion"},
                  12 : {"ley" : "LUC", "art": "129", "if" : "Uniones de Credito"}}
              

        n = int(input("Cuantas preguntas? (max 12)\t"))
        os.system('cls')
        busc = random.sample(list(leyes), n) #Lista de las leyes a preguntar

        score = 0
        error = 0
        for i in busc:
            print("---------------------------Leyes relativas al SFM y DCG a SOB--------\tScore:\t", score, "\tErrores:\t", error)
            resp_ley = input("Ley de: " + str(leyes[i]['if'])+ "\n")    #Ley
            if resp_ley.lower() == leyes[i]["ley"].lower():
                print("Correcto")
                print("------------------------------------------------------------------")
                resp_art = input("Que articulo(s)?\n")
                if resp_art.lower() == leyes[i]['art'].lower():                         #Articulo              
                    score += 1
                    print("Correcto\tScore:\t", score)
                    sleep(2)
                    os.system('cls')
                else:
                    error +=1
                    print("Incorrecto")
                    print("Art. ", leyes[i]['art'])
                    sleep(3)
                    os.system('cls')
                    
            else:
                print("Incorrecto")
                error +=1
                print(leyes[i]["ley"],"Art. ", leyes[i]['art'])
                sleep(3)
                os.system('cls')
                

        calificacion = round((score/n)*100, 2)
        print("------------------------------------------------------")
        print("Calificacion\n\t", calificacion, "%")
        
        cont = input("Deseas intentarlo otra vez? (s/n)\n")
        if cont == 's':
            os.system('cls')
            continue
        else:
            os.system('cls')
            break
                
    return calificacion
