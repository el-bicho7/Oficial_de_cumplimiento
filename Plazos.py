import funcion_preguntas

'''Plazos regulatorios'''

def plazos():
    plazos = {'Revocar Oficial de Cumplimiento todos los SOB' : 'al dia siguiente habil',
              'Designar Oficial de Cumplimiento Interino todos los SOB' : 'al dia siguiente habil por 90 dias naturales',
              'Designar Oficial de Cumplimiento todos los SOB' : '2 dias habiles',
              'Transmisores de acciones por mas del 2% despues del registro' : '3 dias habiles',
              'Persona o grupo de personas que ejercen el control despues de realizar un cambio' : '10 dias habiles',
              'Designacion, Revocacion y Designacion de interino en SOFOM, Inst. de Pago Electronico y Inst de Financiamiento Colectivo' : '10 dias habiles',
              'Designar Representante de Cumplimiento Asesores de Inversion' : '15 dias habiles',
              'Integracion Comite de comunicacion y control' : '15 dias habiles',
              'Designacion, adicion o sustitucion Comite de comunicacion y control' : '15 dias habiles',
              'Persona o grupo de personas que ejercen el control despues de obtener numero de registro' : '20 dias habiles',
              'Modificaciones al Manual de cumplimiento' : '20 dias habiles',
              'Informe de auditoria' : '60 dias naturales',
              'Presentacion de avisos Act. Vulnerable' : 'Primeros 17 dias del mes siguiente'}
              
    tema = "Plazos regulatorios"
    pregunta = "Cuales son los plazos regulatorios para "
    calificacion = funcion_preguntas.preguntas_str(plazos, tema, pregunta)
    return calificacion

