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



def Repa():
    while True:
        print("".center(70, "="))
        print("Que deseas repasar? (Solo opciones disponibles)\n\t1. 40 Recomendaciones","\n\t2. Leyes","\n\t3. Clientes y Usuarios",
            "\n\t4. Regimen Simplificado", "\n\t5. Plazos Regularios", "\n\t6. Umbrales de identificacion",
            "\n\t7. Lineamientos de la auditoria", "\n\t8. Infracciones", "\n\t9. Auditoria",
            "\n\t10. Sistema automatizado, OC y CCC", "\n\t11. Guia EBR para el sector bancario", "\n\t12. Adecuada gestion del riesgo",
            "\n\t13. Obligaciones\t\t\t", "\n\t0. Salir\n")
        n = int(input())
        os.system('cls')

        if n == 1:
            print("".center(70, "="))
            for num, rec in Recomendaciones40.recom.items():
                recom = "Recomendacion {} - {} ({})".format(num, rec[-1],rec[0])
                wrapp = textwrap.fill(recom)
                print(wrapp)
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == 2:
            for num, ley in Leyes.leyes.items():
                print("".center(70, "="))
                for cod, resp in ley.items():
                    ley_wrap = "{} : {}".format(cod.capitalize(), ", ".join(resp))
                    wrapp = textwrap.fill(ley_wrap)
                    print(wrapp)
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == 3:
            for i, j in ClientesUsuarios.clientes.items():
                print("".center(70, "="))
                client = "{} \n-{}".format(i, ", ".join(j))
                wrapp = textwrap.fill(client)
                print(wrapp)
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == 4:
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

        elif n == 5:
            for env, dias in Plazos.plazo.items():
                print("".center(70,"="))
                plazz = "{} - {}".format(env, dias)
                wrapp = textwrap.fill(plazz)
                print(wrapp)
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == 6:
            for lvl, info in Niveles.nivel.items():
                print(lvl)
                levels = "Docs: {}".format(", ".join(info))
                wrapp = textwrap.fill(levels)
                print(wrapp)
                print("".center(70,"="))
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == 7:
            for numero, linea in LineamientosAuditoria.lineamientos.items():
                print("Lineamiento", numero, "-", linea)
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == 8:
            for inf, cond in Infracciones.sancion.items():
                print(inf)
                santion= ", ".join(cond)
                wrapp = textwrap.fill(santion)
                print(wrapp)
                print("".center(70,"="))
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == 9:
            for proced, orden in Auditoria.proced.items():
                print(proced)
                procedd = ", ".join(orden)
                wrapp = textwrap.fill(procedd)
                print(wrapp)
                print("".center(70,"="))

            for proced, orden in Auditoria.orden.items():
                print(proced)
                orders = ", ".join(orden)
                wrapp = textwrap.fill(orders)
                print(wrapp)
                print("".center(70,"="))

            for proced, orden in Auditoria.visitas.items():
                print(proced)
                visits = ", ".join(orden)
                wrapp = textwrap.fill(visits)
                print(wrapp)
                print("".center(70,"="))
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == 10:
            for sist, func in CCCyOC.sistema.items():
                print(sist)
                systems = ", ".join(func)
                wrapp = textwrap.fill(systems)
                print(wrapp)
                print("".center(70,"="))

            for oc, func in CCCyOC.ofc.items():
                print(oc)
                systems = ", ".join(func)
                wrapp = textwrap.fill(systems)
                print(wrapp)
                print("".center(70,"="))

            for comite, func in CCCyOC.ccyc.items():
                print(comite)
                systems = ", ".join(func)
                wrapp = textwrap.fill(systems)
                print(wrapp)
                print("".center(70,"="))
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == 11:
            print("Seccion 1: Elementos clave del EBR")
            for ret, defi in Guia_EBR.retos.items():
                print(ret)
                systems = ", ".join(defi)
                wrapp = textwrap.fill(systems)
                print(wrapp)
                print("".center(70,"="))

            print("Seccion 2: Guia para supervisores")
            for ban, defi in Guia_EBR.bancos.items():
                print(ban)
                systems = ", ".join(defi)
                wrapp = textwrap.fill(systems)
                print(wrapp)
                print("".center(70,"="))

            print("Seccion 3: Guia para banco")
            for sup, defi in Guia_EBR.supervisores.items():
                print(sup)
                systems = ", ".join(defi)
                wrapp = textwrap.fill(systems)
                print(wrapp)
                print("".center(70,"="))
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == 12:
            for i, j in Adecuada_gestion.ele.items():
                print(i)
                for resp in j:
                    print("-", resp)
                print("".center(70,"="))
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == 13:
            for obl, caus in Obligaciones.obligacion.items():
                print(obl)
                systems = ", ".join(caus)
                wrapp = textwrap.fill(systems)
                print(wrapp)
                print("".center(70,"="))
            input("\n\nPresiona Enter para continuar...")
            os.system('cls')

        elif n == 0:
            break

        else:
            print("No es una opcion valida, intenta otra vez\nPresiona Enter para continuar...")
            input()
            os.system('cls')
            continue
