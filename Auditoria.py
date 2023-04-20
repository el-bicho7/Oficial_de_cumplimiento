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

def auditoria():    
    calificacion = { 1 : 0,
                     2 : 0,
                     3 : 0}
    while True:
        
        print("".ljust(80,'-'))
        print("Que quieres practicar?\n\ta. Procedimiento de la Auditoria\t", calificacion[1], "%\n\tb. Orden de visita\t\t\t", calificacion[2],"%\n\tc. Procedimiento de visita de Auditoria\t", calificacion[3], "%\n\td. Salir\n")
        resp = input()
        os.system('cls')
        if resp == 'a':
            calificacion[1] = proced_visita()

        elif resp == 'b':
            calificacion[2] = orden_visita()

        elif resp == 'c':
            calificacion[3] = visita()

        elif resp == 'd':
            break
    c = 0
    for key, value in calificacion.items():
        c += value

    promedio  = round(c/len(calificacion), 2)

    return promedio
        
        
