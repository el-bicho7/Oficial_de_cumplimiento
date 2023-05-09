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


def Repa():
    while True:
        print("".center(70, "="))
        print("Que deseas repasar? (Solo opciones disponibles)",
            "\n\t1. LD y FT\n\t2. 40 Recomendaciones",
            "\n\t3. Leyes\n\t4. Clientes y Usuarios",
            "\n\t5. Regimen Simplificado\n\t6. Plazos Regularios",
            "\n\t7. Umbrales de identificacion",
            "\n\t8. Lineamientos de la auditoria\n\t9. Infracciones",
            "\n\t10. Auditoria\n\t11. Sistema automatizado, OC y CCC",
            "\n\t12. Guia EBR para el sector bancario\n\t13. Adecuada gestion del riesgo",
            "\n\t14. Obligaciones\n\t0. Salir\n")
        n = input()
        os.system('cls')

        if n == "1":
            print("".center(70,"="))
            print("Elige un tema para repasar\n\t1. Definiciones Lavado de dinero\n\t2. Etapas de LD\n\t3. Ejemplos Etapas LD"
            "\n\t4. Diferencia LD y FT\n\t5. Corrupcion\n\t6. Penas LD\n\t7. Penas FT\n\t0. Salir")
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
            elif opcion == '0':
                break
            else:
                print("No es una opcion valida, intenta otra vez\nPresiona Enter para continuar...")
                input()
                os.system('cls')
                continue


        elif n == "2":
            print("".center(70, "="))
            for num, rec in Recomendaciones40.recom.items():
                recom = "Recomendacion {} - {} ({})".format(num, rec[-1],rec[0])
                wrapp = textwrap.fill(recom)
                print(wrapp)
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')


        elif n == "3":
            for num, ley in Leyes.leyes.items():
                print("".center(70, "="))
                for cod, resp in ley.items():
                    ley_wrap = "{} : {}".format(cod.capitalize(), ", ".join(resp))
                    wrapp = textwrap.fill(ley_wrap)
                    print(wrapp)
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == "4":
            imprimir_varios(ClientesUsuarios.clientes.items())
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == "5":
            for act, inf in RegimenSimp.cuenta.items():
                print("".center(70, "="))
                for nivel, docs in inf.items():
                    for udi, doc in docs.items():
                        print("{} es el {}\n \nUDIS: {}".format(act, nivel, udi))
                        reggi = "Docs: {}".format(", ".join(doc))
                        wrapp = textwrap.fill(reggi)
                        print(wrapp)
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == "6":
            for env, dias in Plazos.plazo.items():
                print("".center(70,"="))
                plazz = "{} - {}".format(env, dias)
                wrapp = textwrap.fill(plazz)
                print(wrapp)
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == "7":
            print("Identificacion de clientes:\n")
            imprimir_varios(Niveles.nivel.items())
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == "8":
            print("Lineamientos de la Auditoria")
            for numero, linea in LineamientosAuditoria.lineamientos.items():
                print("Lineamiento", numero, "-", linea)
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == "9":
            imprimir_varios(Infracciones.sancion.items())
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == "10":
            print("Procedimiento de auditoria:\n")
            imprimir_varios(Auditoria.proced.items())
            print()
            print("Orden de visita de la auditoria:\n")
            imprimir_varios(Auditoria.orden.items())
            print()
            print("Procedimiento de la visita:\n")
            imprimir_varios(Auditoria.visitas.items())
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == "11":
            print("Sistema automatizado:\n")
            imprimir_varios(CCCyOC.sistema.items())
            print("Oficial de cumplimiento:\n")
            imprimir_varios(CCCyOC.ofc.items())
            print("Comite de Comunicacion y Control:\n")
            imprimir_varios(CCCyOC.ccyc.items())
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == "12":
            print("Seccion 1: Elementos clave del EBR")
            imprimir_1(Guia_EBR.retos.items())
            print("Seccion 2: Guia para supervisores")
            imprimir_varios(Guia_EBR.bancos.items())
            print("Seccion 3: Guia para banco")
            imprimir_varios(Guia_EBR.supervisores.items())
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == "13":
            imprimir_varios(Adecuada_gestion.ele.items())
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == "14":
            imprimir_varios(Obligaciones.obligacion.items())
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')


        elif n == "0":
            break

        else:
            print("No es una opcion valida, intenta otra vez\nPresiona Enter para continuar...")
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
