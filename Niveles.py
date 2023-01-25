'''Niveles de registro'''
import funcion_preguntas

def niveles():
    niveles = { 'N1 PF' : ['Nombre completo', 'Pais de nacimiento', 'Nacionalidad', 'Fecha de nacimiento', 'Domicilio', '# de ID'],
                    'N2 PF' : ['N1', 'Copia ID'],
                    'N3 PF' : ['N1', 'Ocupacion', 'Genero', 'Estado de nacimiento', '# de telefono', 'e-mail', 'CURP', 'RFC', 'firma electronica', 'Copia ID', 'Copia CURP', 'Copia domicilio', 'Declaracion firmada'],
                    'N1 PM' : ['Denominacion o razon social', 'RFC con Homoclave', 'firma electronica', 'Domicilio', 'Nacionalidad', 'Datos N1 PF'],
                    'N2 PM' : ['N1', 'Copia ID Representante'],
                    'N3 PM' : ['N1', 'Giro Mercantil', '# de telefono', 'e-mail', 'Fecha de constitucion', 'Nombre del admin', 'Copia doc que acredite existencia', 'Copia Cedula fiscal', 'Copia domicilio', 'Poderes'],
                    'N1 Fideicomiso' : ['# de Referencia del fideicomiso', 'Denominacion o razon social del fiduciario', 'Nombre completo apoderado o fiduciario'],
                    'N2 Fideicomiso' : ['N1', 'Copia ID PF'],
                    'N3 Fideicomiso' : ['N1', 'Finalidad del fideicomiso', 'Lugar y fecha del fideicomiso', 'Patrimonio fideicomitido', 'Aportaciones fideicomitentes', 'Datos de ID partes del fideicomiso', 'Copia Constitucion Fideicomiso', 'Copia domicilio', 'Copia Testimonio poderes', 'Copia Cedula ID Fiscal']}

    tema = "Niveles de registro"
    pregunta = "Datos para "
    calificacion = funcion_preguntas.preguntas_list(niveles, tema, pregunta)
    return calificacion
