'''Infracciones'''
import funcion_preguntas

sancion = {"Infracciones Graves" : ["No manual", "No reportes", "No sistema automatizado", "No estructuras internas"],
             "Conducta No Grave" : ["Impacto a terceros", "La Reincidencia", "Cuantia de la operacion", "Condicion economica", "Naturaleza de la infraccion"],
             "Conducta Grave" : ["Monto del quebranto", "Lucro obtenido", "Falta de honorabilidad", "Negligencia inexcusable o dolo", "La conducta sea constitutiva de un delito", "Demas circunstancias"]}


def sanciones():
    
    tema = "Sanciones"
    pregunta = "Cuales son las "
    calificacion = funcion_preguntas.preguntas_list(sancion, tema, pregunta)
    return calificacion
