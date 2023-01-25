import random
import os
from time import sleep

def Recomendaciones():
    recom = { 1 : ["ER EBR", "Evaluacion de riesgos y enfoque basado en riesgo"],
                  2 : ["CCN", "Cooperacion y Coordinacion Nacional"],
                  3 : ["DLA", "Delito de Lavado de Activo"],
                  4 : ["DMP", "Decomiso y Medidas Provisionales"],
                  5 : ["DFT", "Delito Financiamiento al Terrorismo"],
                  6 : ["SFD RTFT", "Sanciones Financieras Designadas Relacionadas al Terrorismo y Financiamiento al Terrorismo"],
                  7 : ["SFD RPADM", "Sanciones Financieras Designadas Relacionadas a la Proliferacion de Armas de Destruccion Masiva"],
                  8 : ["OSFL", "Organizaciones Sin Fines de Lucro"],
                  9 : ["LSIF", "Ley sobre secreto de las Instituciones Financieras"],
                  10 : ["DDC", "Debida Diligencia del Cliente"],
#-----------------------------------------------------------------------
                  11 : ["MR", "Mantenimiento de Registros"],
                  12 : ["PEP", "Personas Expuestas Politicamente"],
                  13 : ["BC","Banca Corresponsal"],
                  14 : ["STDV", "Servicio de tranferencia de valores"],
                  15 : ["NT", "Nuevas tecnologias"],
                  16 : ["TE", "Transferencias electronicas"],
                  17 : ["D3", "Dependencia de terceros"],
                  18 : ["CI FS", "Control Interno de Filiales y Subsidiarias"],
                  19 : ["PMR", "Paises de Mayor Riesgo"],
                  20 : ["ROS", "Reporte de Operacionies Sospechosas"],
#-----------------------------------------------------------------------
                  21 : ["RC", "tipping-off", "Revelacion y Confidencialidad"],
                  22 : ["APNFD DDC", "Actividades y Profesiones No Financieras Deignadas DDC","Actividades y Profesiones No Financieras Deignadas Debida Diligencia del Cliente"],
                  23 : ["APNFD OM", "Actividades y Profesiones No Financieras Deignadas OM","Actividades y Profesiones No Financieras Otras Medidas"],
                  24 : ["TBF PJ", "Transparencia y Beneficiario Final de Personas Juridicas"],
                  25 : ["TBF OEJ", "Transparencia y Beneficiario Final de Otras Estructuras Juridicas"],
                  26 : ["RS IF", "Regulacion y Supervision de las Instituciones Financieras"],
                  27 : ["FS", "Facultades de los Supervisores"],
                  28 : ["RS APNFD", "Regulacion y Supervision de las APNFD", "Regulacion y Supervision de las Actividades y Profesiones No Financieras Deignadas"],
                  29 : ["UIF", "Unidades de Inteligencia Financiera"],
                  30 : ["RAOPIS", "Responsabilidades de las Autoridades de Orden Publico e Investigativas"],
#-----------------------------------------------------------------------
                  31 : ["FAOPIS", "Facultades de las Autoridades de Orden Publico e Investigativas"],
                  32 : ["TEFEC", "Transporte de Efectivo"],
                  33 : ["E", "Estadistica"],
                  34 : ["GR", "Guia y Retroalimentacion"],
                  35 : ["S", "Sanciones"],
                  36 : ["II", "Instrumentos Internacionales"],
                  37 : ["ALM", "Asistencia Legal Mutua"],
                  38 : ["ALM CD", "Asistencia Legal Mutua de Congelamiento y Decomiso"],
                  39 : ["EX", "Extradicion"],
                  40 : ["OFCI", "Otras Formas de Cooperacion Internacional"]}
#-----------------------------------------------------------------------
    calificacion = 0
    while True:
        score = 0
        error = 0
        print("40 Recomendaciones de GAFI".center(80, "-"))

        n = int(input("Cuantas recomendaciones quieres practicar? (max 40) \n"))
        os.system('cls')
        r = random.sample(list(recom), n)
        incorrecto = {}

        for rec in r:
            print("---------------------------40 Recomendaciones de GAFI-----------\tScore:\t", score, "\tErrores:\t", error)
            resp = input("Recomendacion " + str(rec) + ":\t")

            if resp.lower() == recom[rec][0].lower() or resp == recom[rec][1].lower():
                score += 1
                print("Correcto\tScore:\t", score)
                print(recom[rec][1])
                sleep(2)
                os.system('cls')
            else:
                error += 1
                incorrecto[rec] = recom[rec][1]
                print("Incorrecto\t", recom[rec][0], recom[rec][1])
                sleep(3)
                os.system('cls')

        if len(incorrecto) > 0:
            print("".ljust(80, "-"))
            print("Estas fueron tus respuestas incorrectas:")
            for i in sorted(incorrecto):
                print("\tRecomendacion", i, incorrecto[i])
        print("".ljust(80, "-"))
        calificacion = round((score/n)*100, 2)
        print("Calificacion:\n\t" , calificacion, "%")

        cont= input("Deseas intentarlo otra vez? (s/n)\t")
        if cont == "s":
            os.system('cls')
            continue
        if cont == "n":
            os.system('cls')
            break
    return calificacion
