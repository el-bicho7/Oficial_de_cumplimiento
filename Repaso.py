#!/usr/bin/env python
import os
import textwrap
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
import Polclientes
import Reportes


def Repa():
    while True:
        print("".center(70, "="))
        print("\nQue deseas repasar? (Solo opciones disponibles)\n",
            "\n\t1. Etapa 1: Conocimientos basicos",
            "\n\t2. Etapa 2: Conocimientos tecnicos en materia de PLD",
            "\n\t3. Etapa 3: Auditoria",
            "\n\t3. Salir")
        n = input()
        os.system('cls')

        if n == "1":
            while True:
                print("Etapa 1: Conocimientos basicos".center(70,"="))
                print("\nElige un tema para repasar:\n",
                "\n\t1. Definiciones Lavado de dinero",
                "\n\t2. Etapas de LD",
                "\n\t3. Ejemplos Etapas LD"
                "\n\t4. Diferencia LD y FT",
                "\n\t5. Corrupcion",
                "\n\t6. Penas LD",
                "\n\t7. Penas FT",
                "\n\t8. 40 Recomendaciones"
                "\n\t0. Salir")
                opcion = input()
                os.system('cls')

                if opcion == '1':
                    imprimir_varios(LavadoTerror.defLD.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == '2':
                    imprimir_1(LavadoTerror.EtapaLD.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == '3':
                    imprimir_varios(LavadoTerror.preguntas_EtapasLD.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == '4':
                    imprimir_varios(LavadoTerror.dif_ld_ft.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == '5':
                    imprimir_str(LavadoTerror.corrupcion.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == '6':
                    imprimir_str(LavadoTerror.penasLD.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == '7':
                    imprimir_str(LavadoTerror.penasFT.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == '8':
                    print("".center(70, "="))
                    for num, rec in Recomendaciones40.recom.items():
                        recom = "Recomendacion {} - {} ({})".format(num, rec[-1],rec[0])
                        wrapp = textwrap.fill(recom)
                        print(wrapp)
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == '0':
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
                "\n\t1. Leyes aplicables a SOB",
                "\n\t2. Clientes y usuarios de los SOB",
                "\n\t3. Politica de identificacion de Usuarios",
                "\n\t4. Politica de Identificacion de Clientes",
                "\n\t5. Regimen Simplificado",
                "\n\t6. Reportes",
                "\n\t7. Restriccion de dolares (Falta)",
                "\n\t8. Obligaciones",
                "\n\t9. Sistema Automatizado, OC y CCC",
                "\n\t10. Sanciones",
                "\n\t11. Plazos Regulatorios",
                "\n\t0. Salir")
                opcion = input()
                os.system('cls')

                if opcion == "1":
                    for num, ley in Leyes.leyes.items():
                        print("Leyes aplicables a SOB".center(70, "="))
                        for cod, resp in ley.items():
                            ley_wrap = "{} : {}".format(cod.capitalize(), ", ".join(resp))
                            wrapp = textwrap.fill(ley_wrap)
                            print(wrapp)
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "2":
                    imprimir_varios(ClientesUsuarios.clientes.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "3":
                    print("Politica de Identificacion de usuarios:\n")
                    imprimir_varios(Niveles.nivel.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "4":
                    print("Politica de Identificacion de clientes:\n")
                    imprimir_varios(Polclientes.nivel.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "5":
                    for act, inf in RegimenSimp.cuenta.items():
                        print("".center(70, "="))
                        print()
                        for nivel, docs in inf.items():
                            for udi, doc in docs.items():
                                print("{} es el {}\n \nUDIS: {}".format(act, nivel, udi))
                                reggi = "Docs: {}".format(", ".join(doc))
                                wrapp = textwrap.fill(reggi)
                                print(wrapp)
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "6":
                    print("Reportes:\n")
                    imprimir_varios(Reportes.reportes_SOB.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "7":
                    print("Restricciones de dolares (Falta)")
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "8":
                    imprimir_varios(Obligaciones.obligacion.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "9":
                    print("Sistema automatizado:\n")
                    imprimir_varios(CCCyOC.sistema.items())
                    print("Oficial de cumplimiento:\n")
                    imprimir_varios(CCCyOC.ofc.items())
                    print("Comite de Comunicacion y Control:\n")
                    imprimir_varios(CCCyOC.ccyc.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "10":
                    imprimir_varios(Infracciones.sancion.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "11":
                    for env, dias in Plazos.plazo.items():
                        print("".center(70,"="))
                        print()
                        plazz = "{} - {}".format(env, dias)
                        wrapp = textwrap.fill(plazz)
                        print(wrapp)
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "0":
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
                "\n\t1. Lineamientos de Auditoria",
                "\n\t2. Procedimiento de Auditoria",
                "\n\t3. Orden de visita de la Auditoria",
                "\n\t4. Procedimiento de la Visita de Auditoria",
                "\n\t5. Guia EBR",
                "\n\t6. Adecuada gestion del riesgo",
                "\n\t0. Salir")
                opcion = input()
                os.system('cls')

                if opcion == "1":
                    print("Lineamientos de la Auditoria")
                    for numero, linea in LineamientosAuditoria.lineamientos.items():
                        print("Lineamiento", numero, "-", linea)
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "2":
                    print("Procedimiento de auditoria:\n")
                    imprimir_varios(Auditoria.proced.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "3":
                    print("Orden de visita de la auditoria:\n")
                    imprimir_varios(Auditoria.orden.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "4":
                    print("Procedimiento de la visita:\n")
                    imprimir_varios(Auditoria.visitas.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "5":
                    print("Seccion 1: Elementos clave del EBR\n")
                    imprimir_1(Guia_EBR.retos.items())
                    print("Seccion 2: Guia para supervisores\n")
                    imprimir_varios(Guia_EBR.supervisores.items())
                    print("Seccion 3: Guia para banco\n")
                    imprimir_varios(Guia_EBR.bancos.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "6":
                    imprimir_varios(Adecuada_gestion.ele.items())
                    input("\n\nPresiona Enter para continuar...")
                    os.system('cls')
                elif opcion == "0":
                    break
                else:
                    print("No es una opcion valida, intenta otra vez\nPresiona Enter para continuar...")
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

def imprimir_1(libreria): #libreria con una lista de 1 contenido
    for tema, definiciones in libreria:
        print(tema)
        contenido = ", ".join(definiciones)
        wrapp = textwrap.fill(contenido)
        print("-", wrapp)
        print("".center(70,"="))

def imprimir_varios(libreria): #libreria con una lista de varios contenidos
    for tema, definiciones in libreria:
        print(tema)
        for defi in definiciones:
            wrapp = textwrap.fill(defi)
            print("-", wrapp)
        print("".center(70,"="))

def imprimir_str(libreria): #imprimir una libreria
    for tema, definicion in libreria:
        print(tema)
        wrapp = textwrap.fill(definicion)
        print("-", wrapp, "\n")
        print("".center(70,"="))
