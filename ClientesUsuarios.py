import funcion_preguntas

'''Clientes y Usuarios'''
def clientesyusuarios():        
    clientes = { "Clientes y usuarios" : ["SOFIPO", "SOFICO", "SOCAP", "OIF", "Fondo de pago Electronico","Banca Multiple","Banca Desarrollo","Casa de Bolsa"],
                     "Clientes" : ["Sociedad Anonima de Fondo de Inversion", "Asesor de inversion", "Almacen General de Deposito", "SOFOM", "Union de Credito", "Financiamiento Colectivo"],
                     "Usuarios" : ["Centro Cambiario", "Transmisor de dinero", "Casa de Cambio"]}

    tema = "Clientes y Usuarios"
    pregunta = "Que SOB tienen "
        
    calificacion = funcion_preguntas.preguntas_list(clientes, tema, pregunta)
    return calificacion

