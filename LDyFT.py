#!/usr/bin/env python
import random
import os
import textwrap
from time import sleep
import funcion_preguntas

"Practica Lavado de dinero y Financiamiento al terrorismo"

def definicionesLD():
    defLD = {   "Convencion de Viena" : "Conversion o tranferencia de bienes que procedieron de un delito de trafico de drogas.",
                "GAFI" : "Procesamiento de ganancias derivadas de  la act. criminal, disfrazar su procedencia ilicita sin arriesgar su fuente.",
                "VSPP" : "Encubrir el origen de los fondos, generados mediante el ejercicio de algunas actividades ilegales"}

    tema = "Lavado de dinero"
    pregunta = "Esto lo define: "
    calificacion = funcion_preguntas.preguntas_str(defLD, tema, pregunta)

EtapasLD = {"1" : ["Colocacion", "Introduccion", "Localizacion"],
            "2" : ["Estratificacion", "Decantacion", "Ocultamiento", "Enmascaramiento", "Distribucion"],
            "3" : ["Integracion"]}

preguntas_EtapasLD = {  "1" : ["Introduce sus ganancias ilegales al sistema financiero","Dividiendo cantidades de efectivo en sumas mas pequenas y luego se depositan en una cuenta bancaria"],
                        "2" : ["Se involucra una serie de conversiones y movimientos", "Conversion de los fondos procedentes de actividades ilicitas, creando capas de transacciones financieras", "Desligar fondos de su origen"],
                        "3" : ["Reingreso a la economia como transacciones comericales", "Invertir en fondos de bienes raices", "Invertir en articulos de lujo o proyectos comericales"]}

dif_ld_ft = {"LD" : ["Fondos ilicitos", "Proposito es ocultar el origen de los fondos", "El volumen de los recursos es mayor", "Le da oportunidad de incrementar su riqueza", "Objetivo: Actos tendientes a ocultar el origen de los recursos"],
             "FT" : ["Fondos licitos o ilicitos", "Proposito es hacer llegar los recursos a personas", "El volumen es a menor escala", "Objetivo: No es incrementar su riqueza, si no conseguir recursos para financiar sus actividades"]}

corrupcion = {"Corrupcion a gran escala" : "Actos cometidos en los niveles mas altos del gobierno",
              "Actos de corrupcion menor" : "Abuso cotidiano de poder por PEP de bajo y medio rango",
              "Corrupcion politica" : "Manipulacion de politicas, instituciones y normas de procedimiento en la asignacion de recursos y financiamiento"}

penasLD = {"Operaciones con recursos de procedencia ilicita Art. 400 Bis" : "5 a 15 anos y 1000 a 5000 dias de multa",
           "Sujetos al regimen de PLD" : "Se aumenta de 1/3 a 1/2",
           "Servidores publicos" : "Se duplica",
           "Menores de edad" : "Se aumenta hasta 1/2"}

penasFT = {"Delito de terrorismo Art. 139" : "15 a 40 anos y 400 a 1200 dias de multa",
           "Encubrimiento Art. 139 Bis" : "1 a 9 anos y 100 a 300 dias de multa",
           "Amenaza terrorista Art. 139 Ter" : "5 a 15 anos y 200 a 600 dias de multa",
           "Delito de Financiamiento al terrorismo" : "15 a 40 anos y 400 a 1200 dias de multa"}


def LD():
    calificacion = {1 : 0,
                    2 : 0,
                    3 : 0,
                    4 : 0,
                    5 : 0}
    print("".center(70, "="))
    print("Que quieres practicar?\n\ta. Definiciones Lavado de dinero", calificacion[1],
          "\n\tb. Etapas Lavado de Dinero\n\tc. Diferencia LD y FT\n\td. Penas\n\te. Corrupcion\n\tf. Salir")
    resp = input()
    os.system('cls')
    if resp == "a":
        calificacion[1] = definicionesLD()
    elif resp == "b":
        calificacion[2] = etapasLD()
    elif resp == "c":
        calificacion[3] = ldyft_dif()
    elif resp == "d":
        calificacion[4] = penas()
    elif resp == "e":
        calificacion[5] = corrupcion()
    elif resp == "f":
        exit()
    else:
        print("No es opcion valida.")
        sleep(2)
        os.system('cls')
        LD()

LD()
