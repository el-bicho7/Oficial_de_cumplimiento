#!/usr/bin/env python
import random
import os
import textwrap
from time import sleep
import funcion_preguntas

"Practica Lavado de dinero y Financiamiento al terrorismo"

defLD = {   "Viena" : ["Conversion o tranferencia de bienes que procedieron de un delito de trafico de drogas (narcotrafico)", "La ocultacion o el encubrimiento de la naturaleza, el origen, la ubicacion, el destino, el movimiento o la propiedad reales de bienes, sabiendo que proceden de alguno de los delitos del narcotrafico"],
                "GAFI" : ["Procesamiento de ganancias derivadas de  la act. criminal, disfrazar su procedencia ilicita sin arriesgar su fuente"],
                "VSPP" : ["Encubrir el origen de los fondos, generados mediante el ejercicio de algunas actividades ilegales"],
                "Palermo" : ["La adquisicion, posesion o utilizacion de bienes, a sabiendas, en el momento de su recepcion, de que son producto del delito"]}

EtapaLD = { "Etapa 1" : ["Colocacion", "Introduccion", "Localizacion"],
            "Etapa 2" : ["Estratificacion", "Decantacion", "Ocultamiento", "Enmascaramiento", "Distribucion"],
            "Etapa 3" : ["Integracion"]}

preguntas_EtapasLD = {  "Etapa 1" : ["Introduce sus ganancias ilegales al sistema financiero",
                                    "Dividiendo cantidades de efectivo en sumas mas pequenas y luego se depositan en una cuenta bancaria"],
                        "Etapa 2" : ["Se involucra una serie de conversiones y movimientos",
                                    "Conversion de los fondos procedentes de actividades ilicitas, creando capas de transacciones financieras",
                                    "Desligar fondos de su origen", "Realizar transferencias bancarias de una cuenta a otra, a veces entre distintas instituciones o países."],
                        "Etapa 3" : ["Reingreso a la economia como transacciones comericales",
                                    "Invertir en fondos de bienes raices", "Invertir en articulos de lujo o proyectos comericales",
                                    "Liquidar anticipadamente un crédito hipotecario con dinero en efectivo de procedencia ilícita, para posteriormente venderlo."]}

dif_ld_ft = {"LD" : ["Fondos ilicitos", "Proposito es ocultar el origen de los fondos", "El volumen de los recursos es mayor", "Le da oportunidad de incrementar su riqueza", "Objetivo: Actos tendientes a ocultar el origen de los recursos"],
             "FT" : ["Fondos licitos o ilicitos", "Proposito es hacer llegar los recursos a personas", "El volumen es a menor escala", "Objetivo: No es incrementar su riqueza, si no conseguir recursos para financiar sus actividades"]}

corrupcion = {"Corrupcion a gran escala" : "Actos cometidos en los niveles mas altos del gobierno",
          "Actos de corrupcion menor" : "Abuso cotidiano de poder por PEP de bajo y medio rango",
          "Corrupcion politica" : "Manipulacion de politicas, instituciones y normas de procedimiento en la asignacion de recursos y financiamiento"}

penasLD = {"Operaciones con recursos de procedencia ilicita Art. 400 Bis" : "5 a 15 anos y 1000 a 5000 dias de multa",
           "Sujetos al regimen de PLD" : "Aumenta de 1/3 a 1/2",
           "Servidores publicos" : "Se duplica",
           "Menores de edad" : "Aumenta hasta 1/2"}


penasFT = {"Delito de terrorismo Art. 139" : "15 a 40 anos y 400 a 1200 dias de multa",
           "Encubrimiento Art. 139 Bis" : "1 a 9 anos y 100 a 300 dias de multa",
           "Amenaza terrorista Art. 139 Ter" : "5 a 15 anos y 200 a 600 dias de multa",
           "Delito de Financiamiento al terrorismo" : "15 a 40 anos y 400 a 1200 dias de multa"}


def definicionesLD():

    tema = "Lavado de dinero"
    pregunta = "Esto lo define:\n(Opciones: GAFI, Palermo, Viena, VSPP)\n"
    calificacion = funcion_preguntas.preguntas_1_resp_list(defLD, tema, pregunta)
    return calificacion

def etapasLD():

    tema = "Etapas de lavado de dinero"
    pregunta = "Contesta a que etapa de lavado de dinero pertenece:\n(Etapa 1, Etapa 2, Etapa 3)\n"
    calificacion = funcion_preguntas.preguntas_1_resp_list(EtapaLD, tema, pregunta)
    return calificacion

def difetapas():

    tema = "Etapas de Lavado de  Dinero"
    pregunta = "Contesta a que etapa de lavado de dinero pertenece:\n(Etapa 1, Etapa 2, Etapa 3)\n"
    calificacion = funcion_preguntas.preguntas_1_resp_list(preguntas_EtapasLD, tema, pregunta)
    return calificacion

def ldyft_dif():

    tema = "Diferencias de Lavado de dinero y Financiamiento al terrorismo"
    pregunta = "Contesta a que pertenece:\n(LD o FT)\n"
    calificacion = funcion_preguntas.preguntas_1_resp_list(dif_ld_ft, tema, pregunta)
    return calificacion

def Corrupcion():

    tema = "Corrupcion"
    pregunta = "A que tipo de corrupcion pertenece: \n"
    calificacion = funcion_preguntas.preguntas_sstr(corrupcion, tema, pregunta)
    return calificacion

def Penas_LD():

    tema = "Penas LD"
    pregunta = "Pena para: \n"
    calificacion = funcion_preguntas.preguntas_str(penasLD, tema, pregunta)
    return calificacion

def Penas_FT():

    tema = "Penas FT"
    pregunta = "Pena para: \n"
    calificacion = funcion_preguntas.preguntas_sstr(corrupcion, tema, pregunta)
    return calificacion
