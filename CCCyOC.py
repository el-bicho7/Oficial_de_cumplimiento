#!/usr/bin/env python
'''CCC y OC'''
import funcion_preguntas
import os

sistema = {"Sistema automatizado" : ["Deteccion seguimiento y analisis op inusuales", "Registro historico op inusuales", "Medio para reportar op inusuales", "Mantener esquemas de seguridad", "Proveer info de la metodologia",
    "Generar y transmitir info de los reportes", "Conservar y actualizar expedientes", "Facilitar verificacion de datos y documentos",
    "Detectar y monitorear las op de un mismo cliente", "Agrupar clientes y usuarios", "Alertas sobre comportamiento transaccional", "Lista PEP bloqueadas y paises de riesgo",
    "Clasificar las operaciones", "Permitir trazabilidad y origen"]}

ofc = {"Oficial de cumplimiento" : ["Elaborar y someter a consideracion el manual", "Someter aprobracion la metodologia", "Enviar reportes op", "Hacer conocimiento al comite las cuentas de alto riesgo",
    "Coordinar las actividades de seguimiento", "Definir el contenido y alcance de la capacitacion", "Informar al CCC sobre conductas que provoquen infraccion",
    "Recibir y verificar que la entidad de respuesta a los requerimientos de informacion", "Instancia de consult respecto a las disposiciones y manual", "Enlace entre CCC SHCP y CNBV"
    "Verificar correcta ejecucion de medidas del CCC"]}


ccyc = {"Comite de Comunicacion y control" : ["Aprobar Manual de cumplimiento", "Presentar la metodologia elaborada e implementada al administrador", "Conocer los resultados de la auditoria interna",
    "Conocer cuando una cuenta genera alto riesgo", "Establecer criterios para clasificar clientes en funcion del grado de riesgo", "Los sistemas contengan las listas oficiales",
    "Dictaminar operaciones", "Aprobar programas de capacitacion", "Informar sobre conductas de directivos que provoquen una infraccion", "Asegurar que se cuenta con recursos para cumplimiento",
    "Asegurar que se solicite y mantenga la cuenta SITI a nombre del oc"]}

def sist_autom():

    tema = "Sistema automatizado"
    pregunta = "Funciones del "
    calificacion = funcion_preguntas.preguntas_list(sistema, tema, pregunta)
    return calificacion

def OC():
          
    tema = "Oficial de cumplimiento"
    pregunta = "Funciones del "
    calificacion = funcion_preguntas.preguntas_list(ofc, tema, pregunta)
    return calificacion
    
def CCC():
      
    tema = "Comite de Comunicacion y Control"
    pregunta = "Funciones del "
    calificacion = funcion_preguntas.preguntas_list(ccyc, tema, pregunta)
    return calificacion

def funciones():
    calificacion = { 1 : 0,
                     2 : 0,
                     3 : 0}
    while True:
        print("".ljust(80, "-"))
        print("Que quieres practicar?\n\ta. Sistema automatizado\t\t\t", calificacion[1], "%\n\tb. Oficial de cumplimiento\t\t", calificacion[2],"%\n\tc. Comite de Comunicacion y Control\t", calificacion[3], "%\n\td. Salir\n")
        resp = input()
        os.system('cls')
        if resp == 'a':
            calificacion[1] = sist_autom()

        elif resp == 'b':
            calificacion[2] = OC()

        elif resp == 'c':
            calificacion[3] = CCC()

        elif resp == 'd':
            break
    c = 0
    for key, value in calificacion.items():
        c += value

    promedio  = round(c/len(calificacion), 2)

    return promedio
        
