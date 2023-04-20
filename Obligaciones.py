#!/usr/bin/env python
'''Obligaciones'''
import funcion_preguntas

obligacion = {"Obligaciones" : ["Capacitacion y difusion", "Reserva y confidencialidad", "Seleccion de personal", "Conservacion de informacion", "Auditor interno y externo independiente",
                "Manual de cumplimiento"]}

def obligaciones():

    pregunta = "Cuales son las "
    tema = "Obligaciones"

    funcion_preguntas.preguntas_list(obligacion, tema, pregunta)

