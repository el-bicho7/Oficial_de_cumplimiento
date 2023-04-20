#!/usr/bin/env python
'''Lineamientos auditoria'''
import funcion_preguntas

lineamientos = { "1" : "Objeto",
                 "2" : "Definiciones",
                 "3" : "Interpretacion y consultas",
                 "4" : "Requisitos que debe reunir el auditor",
                 "5" : "Requisitos que debe reunir la PM",
                 "6" : "Planeacion de la auditoria",
                 "7" : "Programa de trabajo",
                 "8" : "Secciones del informe",
                 "9" : "Redaccion y estructura del informe",
                 "10" : "Pruebas y documentos sustento del informe",
                 "11" : "Conocimiento y remision del informe",
                 "12" : "Conservacion"}

def lin_auditoria():
    

    tema = "Lineamientos auditoria"
    pregunta = "Cual es el lineamiento "
    calificacion = funcion_preguntas.preguntas_str(lineamientos, tema, pregunta)
    return calificacion
