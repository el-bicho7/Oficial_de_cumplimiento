#!/usr/bin/env python
import random
import os
from time import sleep

cuenta = { "Depositos en MNX" : { "Nivel 1" : {"750 a 1000" : ["Nombre completo", "Fecha de nacimiento"]}},
           "PF Presencial": {"Nivel 2" : {"3000" : ["Nombre completo", "Fecha de nacimiento", "Domicilio"]}},
           "PF Remota" : {"Nivel 2" : {"3000" : ["Nombre completo", "Fecha de nacimiento", "Domicilio", "Genero", "Estado de nacimiento"]}},
           "PF Prog Gob" : {"Nivel 2" : {"6000" : ["Nombre completo", "Fecha de nacimiento", "Domicilio", "Genero", "Estado de nacimiento"]}},
           "PF Nomina o credito" : {"Nivel 2" : {"15000" : ["Nombre completo", "Fecha de nacimiento", "Domicilio", "Genero", "Estado de nacimiento"]}},
           "PF, Cuenta Dep, Presencial y remota, edad 15-18" : {"Nivel 2" : {"3000" : ["Nombre completo", "Fecha de nacimiento", "Domicilio", "Genero", "Estado de nacimiento", "# de telefono", "e-mail","Prog Gob"]}},
           "PF y PM Presencial, Transf electronica" : {"Nivel 3" : {"10000" : ["N3 exeptuando copias"]}}}

def Regimen_sim():
    conti = 0
    
    while conti == 0:
        print("Regimen Simplificado Bajo Riesgo".center(80, "-"))
                      
        busc = random.choice(list(cuenta.keys())) #Lista de tipo de cuenta
        score = 0
        
        for nivel, vals in cuenta[busc].items():
            resp1 = input("Hasta que nivel aplica el regimen simplificado en " + busc + ":\t")
            if resp1.lower() == nivel.lower():
                print("Correcto")
                                
            else:
                print("Incorrecto\t", "\tRespuesta:\t", nivel)
                                
                
        print("".center(80,"-"))    
        
        for udi, datos in vals.items():
            resp2 = input("Cuantos UDIS al mes:\t")    
            if resp2.lower() == udi.lower():
                print("Correcto")
                sleep(1)
                os.system('cls')
                
            else:
                print("Incorrecto\tRespuesta:\t", udi)
                sleep(3)
                os.system('cls')
                        
        new_c = []
        error = 0
        while (len(datos)) > 0:
            print("Regimen Simplificado Bajo Riesgo".center(80, "-"))
            print("Cuales son los datos de identificacion que se solicitan para " + busc)
            print("\tScore:", score, "\tFaltan:\t", len(datos), "\tErrores:\t", error)
            resp3 = input().lower()
            datos = list(map(lambda z: z.casefold(), datos))
            if resp3 not in new_c:
                if resp3 in datos:
                    inde = datos.index(resp3)
                    new_c.append(datos.pop(inde))
                    print("Correcto")               
                    score += 1
                    sleep(1)
                    os.system('cls')
                else:
                    error += 1
                    print("Incorrecto")
                    sleep(2)
                    os.system('cls')
                    if error == 3:
                        print(", ".join(datos))
                        break
                    
            else:
                print("Repetida")
                sleep(2)
                os.system('cls')
                
        calificacion = round((score/(score+error))*100, 2)
        print("".center(80,"-")) 
        print("Calificacion:\n\t" , calificacion, "%")
        cont = input("Deseas intentarlo otra vez? (s/n)\t")
        if cont == 's':
            error = 0
            os.system('cls')
            continue
        if cont == 'n':
            os.system('cls')
            break
            
    return calificacion
