#!/usr/bin/env python3
'''Adecuada gestion del riesgo'''
import funcion_preguntas
import os


def elementos():

    elementos = {"Elementos esenciales de una solida gestion del riesgo BC/FT" : ["Evaluacion comprension gestion y mitigacion de riesgo", "Politicas de aceptacion de clientes", "Identificacion verificacion y elaboracion del perfil de riesgo de clientes",
                                                                                  "Seguimiento continuo", "Gestion de la informacion", "Notificacion de operaciones sospechosas y bloqueo de activos"],
                 "PBC/FT a escala de grupo y un contexto transfronterizo" : ["Proceso global para la gestion del riesgo de clientes", "Evaluacion y gestion del riesgo", "Politicas y procedimientos a escala consolidada",
                                                                               "Intercambio de informacion dentro del grupo", "Grupos financieros mixtos"],
                 "El papel de los supervisores" : ["Desarrollen un conocimiento exhaustivo de los riesgos presentes en la jurisdiccion", "Estimen la suficiencia de la evaluacion", "Evaluen los riesgos presentes en la entidad", "Evaluen la suficiencia y eficacia de la app de controles",
                                                   "Utilicen esa informacion para asignar recursos"]}

    pregunta = ""
    tema = "Adecuada gestion del riesgo"
    instrucciones = "Solo contestar con la respuesta exacta"
    calificacion = funcion_preguntas.preguntas_list(elementos, tema, pregunta, instrucciones)
    return calificacion
