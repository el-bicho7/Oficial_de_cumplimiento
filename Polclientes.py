#!/usr/bin/env python
'''Politica de identificacion de clientes'''
import funcion_preguntas

nivel = {   'PF Nacional Presencial' : ["N3", "Sin # de id"],
            'PF Extranjera Presencial' : ["N3", "Entidad federativa"],
            'PF (Nac o Ext) No Presencial' : ["Consentimiento celebracion de contrato", "Consentimiento dato de geolocalizacion", "e-mail o telefono", "# de Cuenta o CLABE", "Clave del elector", "Copia ID", "Copia domicilio"],
            'PM Nacional Presencial' : ["N3"],
            'PM Extranjera Presencial' : ["N3", "Sin dato del administrador"],
            'PM (Indeterminado) No Presencial' : ["Consentimiento celebracion de contrato", "Consentimiento dato de geolocalizacion", "e-mail", "# de Cuenta o CLABE", "Informacion adicional", "Copia N3", "Firma electronica"],
            'Fideicomiso Presencial' : ['N3'],
            'Proveedor de recursos PF Presencial' : ['N1', 'Ocupacion'],
            'Proveedor de recursos PM Presencial' : ['N1', 'Sin dato de Representante legal'],
            'Entidades Anexo 1 Presencial' : ['N3', 'Sin Fecha de constitucion', 'Sin Giro Mercantil', 'Sin Informacion inciso c', 'Copia poderes', 'ID Representante'],
            'Cotitulares o terceros autorizados' : ['N3'],
            'Beneficiarios' : ["Nombre completo", "Domicilio", "Fecha de nacimiento"],
            'Propietario Real Presencial o No Presencial' : ["N3"]
            }


def niveles():

    tema = "Politica de identificacion de clientes"
    pregunta = "Datos para "
    calificacion = funcion_preguntas.preguntas_list(nivel, tema, pregunta)
    return calificacion
