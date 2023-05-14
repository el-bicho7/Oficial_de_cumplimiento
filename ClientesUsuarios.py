#!/usr/bin/env python
import funcion_preguntas

'''Clientes y Usuarios'''
clientes = { "Clientes y usuarios" : ["SOFIPO", "SOFICO", "SOCAP", "OIF", "IFOPAE","Banca Multiple","Banca Desarrollo","Casa de Bolsa"],
             "Clientes" : ["Sociedad Anonima de Fondo de Inversion", "Asesor de inversion", "Almacen General de Deposito", "SOFOM", "Union de Credito", "IFIC", "FINDARFP"],
             "Usuarios" : ["Centro Cambiario", "Transmisor de dinero", "Casa de Cambio"]}

def clientesyusuarios():


    tema = "Clientes y Usuarios"
    pregunta = "Que SOB tienen "

    calificacion = funcion_preguntas.preguntas_list(clientes, tema, pregunta)
    return calificacion
