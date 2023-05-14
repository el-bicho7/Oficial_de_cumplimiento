#!/usr/bin/env python
import os
import Recomendaciones40
import Leyes
import ClientesUsuarios
import RegimenSimp
import Plazos
import Niveles
import LineamientosAuditoria
import Infracciones
import Auditoria
import CCCyOC
import Guia_EBR
import Adecuada_gestion
import Obligaciones
import LavadoTerror

calificacion_1 = { 1 : 0,
                 2 : 0,
                 3 : 0,
                 4 : 0,
                 5 : 0,
                 6 : 0,
                 7 : 0,
                 8 : 0
                 }

calificacion_2 = { 1 : 0,
                 2 : 0,
                 3 : 0,
                 4 : 0,
                 5 : 0,
                 6 : 0,
                 7 : 0,
                 8 : 0,
                 9 : 0,
                 10: 0,
                 11: 0,
                 12: 0,
                 13: 0
                 }

calificacion_3 = { 1 : 0,
                 2 : 0,
                 3 : 0,
                 4 : 0,
                 5 : 0,
                 6 : 0
                 }

def Est():
    while True:

        print(" Estudio Examen CNBV ".center(80, "="))
        print("\nQue deseas repasar? (Solo opciones disponibles)\n",
            "\n\t1. Etapa 1: Conocimientos basicos",
            "\n\t2. Etapa 2: Conocimientos tecnicos en materia de PLD",
            "\n\t3. Etapa 3: Auditoria",
            "\n\t0. Salir")
        n = input()
        os.system('cls')

        if n == "1":
            while True:
                print("Etapa 1: Conocimientos basicos".center(70,"="))
                print("\nElige un tema para repasar:\n",
                "\n\t1. Definiciones Lavado de dinero\t", calificacion_1[1],
                "%\n\t2. Etapas de LD\t\t\t\t", calificacion_1[2],
                "%\n\t3. Ejemplos Etapas LD\t\t\t", calificacion_1[3],
                "%\n\t4. Diferencia LD y FT\t\t\t", calificacion_1[4],
                "%\n\t5. Corrupcion\t\t\t\t", calificacion_1[5],
                "%\n\t6. Penas LD\t\t\t\t", calificacion_1[6],
                "%\n\t7. Penas FT\t\t\t\t", calificacion_1[7],
                "%\n\t8. 40 Recomendaciones\t\t\t", calificacion_1[8],
                "%\n\t0. Salir")
                opcion1 = input()
                os.system('cls')

                if opcion1 == '1':
                    calificacion_1[1] = LavadoTerror.definicionesLD()

                elif opcion1 == '2':
                    calificacion_1[2] = LavadoTerror.etapasLD()

                elif opcion1 == '3':
                    calificacion_1[3] = LavadoTerror.difetapas()

                elif opcion1 == '4':
                    calificacion_1[4] = LavadoTerror.ldyft_dif()

                elif opcion1 == '5':
                    calificacion_1[5] = LavadoTerror.Corrupcion()

                elif opcion1 == '6':
                    calificacion_1[6] = LavadoTerror.Penas_LD()

                elif opcion1 == '7':
                    calificacion_1[7] = LavadoTerror.Penas_FT()

                elif opcion1 == '8':
                    calificacion_1[8] = Recomendaciones40.Recomendaciones()

                elif opcion1 == '0':
                    break

                else:
                    print("No es una opcion valida, intenta otra vez\nPresiona Enter para continuar...")
                    input()
                    os.system('cls')
                    continue

        elif n == "2":
            while True:
                print("Etapa 2: Conocimientos tecnicos en materia de PLD".center(70,"="))
                print("\nElige un tema para repasar:\n",
                "\n\t1. Leyes aplicables a SOB\t\t\t", calificacion_2[1],
                "%\n\t2. Clientes y usuarios de los SOB\t\t", calificacion_2[2],
                "%\n\t3. Politica de identificacion de Usuarios\t", calificacion_2[3],
                "%\n\t4. Politica de Identificacion de Clientes\t", calificacion_2[4],
                "%\n\t5. Regimen Simplificado\t\t\t\t", calificacion_2[5],
                "%\n\t6. Reportes\t\t\t\t\t", calificacion_2[6],
                "%\n\t7. Restriccion de dolares (Falta)", calificacion_2[7],
                "%\n\t8. Obligaciones\t\t\t\t\t", calificacion_2[8],
                "%\n\t9. Sistema Automatizado\t\t\t\t", calificacion_2[9],
                "%\n\t10. Oficial de Cumplimiento\t\t\t", calificacion_2[10],
                "%\n\t11. Comite Comunicacion y Ccontrol\t\t", calificacion_2[11],
                "%\n\t12. Sanciones\t\t\t\t\t", calificacion_2[12],
                "%\n\t13. Plazos Regulatorios\t\t\t\t", calificacion_2[13],
                "%\n\t0. Salir")
                opcion2 = input()
                os.system('cls')

                if opcion2 == '1':
                    calificacion_2[1] = Leyes.Leyes()

                elif opcion2 == '2':
                    calificacion_2[2] = ClientesUsuarios.clientesyusuarios()

                elif opcion2 == '3':
                    calificacion_2[3] = Polusuarios.niveles()

                elif opcion2 == '4':
                    calificacion_2[4] = Polclientes.niveles()

                elif opcion2 == '5':
                    calificacion_2[5] = RegimenSimp.Regimen_sim()

                elif opcion2 == '6':
                    calificacion_2[6] = Reportes.Reportes()

                elif opcion2 == '7':
                    calificacion_2[7] = Restricciones.Restricciones()

                elif opcion2 == '8':
                    calificacion_2[8] = Obligaciones.obligaciones()

                elif opcion2 == '9':
                    calificacion_2[9] = CCCyOC.sist_autom()

                elif opcion2 == '10':
                    calificacion_2[10] = CCCyOC.OC()

                elif opcion2 == '11':
                    calificacion_2[11] = CCCyOC.CCC()

                elif opcion2 == '12':
                    calificacion_2[12] = Infracciones.sanciones()

                elif opcion2 == '13':
                    calificacion_2[13] = Plazos.plazos()

                elif opcion2 == '0':
                    break

                else:
                    print("No es una opcion valida, intenta otra vez\nPresiona Enter para continuar...")
                    input()
                    os.system('cls')
                    continue

        elif n == "3":
            while True:
                print("Etapa 3: Auditoria".center(70,"="))
                print("\nElige un tema para repasar\n",
                "\n\t1. Lineamientos de Auditoria\t\t\t", calificacion_3[1],
                "%\n\t2. Procedimiento de Auditoria\t\t\t", calificacion_3[2],
                "%\n\t3. Orden de visita de la Auditoria\t\t", calificacion_3[3],
                "%\n\t4. Procedimiento de la Visita de Auditoria\t", calificacion_3[4],
                "%\n\t5. Guia EBR\t\t\t\t\t", calificacion_3[5],
                "%\n\t6. Adecuada gestion del riesgo\t\t\t", calificacion_3[6],
                "%\n\t0. Salir")
                opcion3 = input()
                os.system('cls')

                if opcion3 == '1':
                    calificacion_3[1] = LineamientosAuditoria.lin_auditoria()

                elif opcion3 == '2':
                    calificacion_3[2] = Auditoria.proced_visita()

                elif opcion3 == '3':
                    calificacion_3[3] = Auditoria.orden_visita()

                elif opcion3 == '4':
                    calificacion_3[4] = Auditoria.visita()

                elif opcion3 == '5':
                    calificacion_3[5] = Guia_EBR.guia()

                elif opcion3 == '6':
                    calificacion_3[6] = Adecuada_gestion.elementos()

                elif opcion3 == '0':
                    break

                else:
                    print("\nNo es una opcion valida, intenta otra vez\nPresiona Enter para continuar...")
                    input()
                    os.system('cls')
                    continue

        elif n == "0":
            break

        else:
            print("\nNo es una opcion valida, intenta otra vez\nPresiona Enter para continuar...")
            input()
            os.system('cls')
            continue
