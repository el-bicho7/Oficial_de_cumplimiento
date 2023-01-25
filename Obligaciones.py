'''Obligaciones'''
import funcion_preguntas

def obligaciones():
    obligaciones = {"Obligaciones" : ["Capacitacion y difusion", "Reserva y confidencialidad", "Seleccion de personal", "Conservacion de informacion", "Auditor interno y externo independiente",
                    "Manual de cumplimiento"]}
    pregunta = "Cuales son las "
    tema = "Obligaciones"

    funcion_preguntas.preguntas_list(obligaciones, tema, pregunta)

