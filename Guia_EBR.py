'''EBR'''
import funcion_preguntas
import os

retos = {"Reto 1" : ["Asignacion de responsabilidades"],
         "Reto 2" : ["Identificacion del riesgo"],
         "Reto 3" : ["Evaluacion del riesgo"],
         "Reto 4" : ["Mitigacion del riesgo"],
         "Reto 5" : ["Desarrollo de un entendimiento en comun"],
         "Reto 6" : ["Inclusion financiera"]}

supervisores = { "En general" : ["Entender los riesgos de sus paises", "Asignar recursos a las areas de mayor riesgo", "Entender los riesgos a los que el sector bancario esta expuesto",
                                 "Analizar su evaluacion de perfil periodicamente", "Utilizar hallazgos para revisar y actualizar sus evaluaciones"],
                 "Comprension del riesgo en el caso de riesgos sectoriales" : ["Evaluacion del riesgo", "Tipologias nacionales", "Experiencia de la supervision", "Retroalimentacion de la UIF"],
                 "En el caso de los bancos" : ["El nivel de riesgo inherente", "La naturaleza y complejidad de los productos", "El tamano modelo de negocio y sistemas", "La informacion financiera contable",
                                               "Los canales de distribucion", "Los perfiles de los clientes", "La localizacion geografica y los paises de operacion", " Los controles vigentes"],
                 "Mitigacion del riesgo" : ["Intensidad de los controles", "Tipo de supervision en materia de ala/cft", "Frecuencia y naturaleza de una supervision", "Intensidad de la supervision en materia de ala/cft"]}

bancos = { "Identificacion y Evaluacion del riesgo" : ["La naturaleza escala y complejidad de su actividad", "Mercados destino", "Numero de clientes de alto riesgo",
                                                       "Canales de distribucion", "Auditoria interna", "Volumen y tamano de sus operaciones", "Jurisdicciones que regulan al banco"],
           "Mitigacion del riesgo" : ["DDC y monitoreo", "Actualizar los perfiles de riesgo del cliente", "Cumplir con sanciones", "Verificacion de nombres mediante las listas"],
           "Controles internos" : ["Acuerdos de gobierno corporativo", "Controles para monitorear la integridad del personal"]}
           
    

def seccion_1():
    pregunta = "Cual es el "
    tema = "Seccion 1: Elementos clave del EBR"
    calificacion = funcion_preguntas.preguntas_str(retos, tema, pregunta)
    return calificacion

def seccion_2():
    tema = "Seccion 2: Guia para supervisores"
    pregunta = "Guia para supervisores "
    calificacion = funcion_preguntas.preguntas_list(supervisores, tema, pregunta)
    return calificacion

def seccion_3():
    tema = "Seccion 3: Guia para bancos"
    pregunta = ""
    calificacion = funcion_preguntas.preguntas_list(bancos, tema, pregunta)
    return calificacion

def guia():
    calificacion = { 1 : 0,
                     2 : 0,
                     3 : 0}
    while True:
        print("".center(80, "-"))
        print("Que quieres practicar?\n\ta. Seccion 1: Elementos clave del EBR\t\t", calificacion[1], "%\n\tb. Seccion 2: Guia para supervisores\t\t", calificacion[2],"%\n\tc. Seccion 3: Guia para bancos\t\t\t", calificacion[3], "%\n\td. Salir\n")
        resp = input()
        os.system('cls')
        if resp == 'a':
            calificacion[1] = seccion_1()

        elif resp == 'b':
            calificacion[2] = seccion_2()

        elif resp == 'c':
            calificacion[3] = seccion_3()

        elif resp == 'd':
            break
    c = 0
    for key, value in calificacion.items():
        c += value

    promedio  = round(c/len(calificacion), 2)

    return promedio
        
        
