#!/usr/bin/env python
'''Reportes'''
import funcion_preguntas

reportes_SOB = {"Operaciones Inusuales" : ["Todos los SOB"],
            "24 horas" : ["Todos los SOB"],
            "Internas preocupantes": ["Todos los SOB"],
            "Relevantes" : ["Todos los SOB"],
            "Dolares en efectivo" : ["SOFIPO", "SOFICO", "SOCAP", "Banca Multiple", "Banca Desarrollo", "Casa de Bolsa", "Casa de Cambio", "Centro Cambiario", "Union de credito", "FINDARFP"],
            "Transferencia Internacional de fondos" : ["SOFIPO", "SOFICO", "SOCAP", "Banca Multiple", "Banca Desarrollo", "Casa de Bolsa", "Casa de Cambio", "Centro Cambiario", "Transmisor de dinerro", "Fondo de pago electronico", "Financiamiento Colectivo"],
            "Operaciones en Moneda Extranjera" : ["Fondo de pago electronico", "Financiamiento Colectivo"],
            "Cheques de caja" : ["Banca Multiple", "Banca Desarrollo"],
            "Montos totales" : ["Centro Cambiario"],
            "Operacion con activos virtuales" : ["Banca Multiple", "Banca Desarrollo", "Fondo de pago electronico", "Financiamiento Colectivo"]}

reportes_plazo = {"Operaciones Inusuales" : [],
            "24 horas" : [],
            "Internas preocupantes": [],
            "Relevantes" : [],
            "Dolares en efectivo" : [],
            "Transferencia Internacional de fondos" : [],
            "Operaciones en Moneda Extranjera" : [],
            "Cheques de caja" : [],
            "Montos totales" : [],
            "Operacion con activos virtuales" : []}

def Reportes():

    tema = "Reportes"
    pregunta = "A quien aplica este reporte: "
    calificacion = funcion_preguntas.preguntas_list(nivel, tema, pregunta)
    return calificacion
