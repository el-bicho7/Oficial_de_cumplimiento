#!/usr/bin/env python
'''Auditoria'''

import funcion_preguntas
import os

proced = {"Procedimiento de la auditoria" : ["Orden de visita", "Acta de inicio", "Solicitud para nombrar 2 testigos", "Se elabora una relacion de la informacion y documentacion",
             "Acta parcial", "Acta de conclusion"]}

orden = {"Orden de visita de la Auditoria" : ["Lugar y fecha", "Numero de Oficio", "Nombre entidad supervisada", "Tipo de visita y objeto", "Fecha y duracion menor a 6 meses",
            "Lugares donde se efectuara la visita", "Domicilio de la entidad", "Relacion de la informaicon y documentacion oficial",
            "Nombre del inspector", "Nombre cargo y firma del funcionario que ordeno la visita"]}

visitas = {"Procedimiento de la visita" : ["El inspector se identifica", "El SOB debe permitir la visita", "Dar acceso al lugar", "Proporcionar un espacio fisico",
          "En un solo dia se consta su inicio y conclusion en la misma acta", "Cada acta firmada por el representante legal"]}

def proced_visita():

    tema = "Procedimiento de la Auditoria"
    pregunta = "Cual es el "
    calificacion = funcion_preguntas.preguntas_list(proced, tema, pregunta)
    return calificacion


def orden_visita():

    tema = "Orden de Visita de la Auditoria"
    pregunta = "Cual es el "
    calificacion = funcion_preguntas.preguntas_list(orden, tema, pregunta)
    return calificacion

def visita():

    tema = "Procedimiento de la visita de Auditoria"
    pregunta = "Cual es el "
    calificacion = funcion_preguntas.preguntas_list(visitas, tema, pregunta)
    return calificacion
