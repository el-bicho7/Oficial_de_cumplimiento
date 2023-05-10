#!/usr/bin/env python
import os
import Estudio
import Repaso
import textwrap


def Oficialdecumplimiento():
    while True:
        print(" Oficial de cumplimiento ".center(70, "="))
        print()
        instrucciones = "Programa para Estudiar y/o Repasar los temas que se veran en el examen del Oficial de cumplimiento.\n"
        wrapp = textwrap.fill(instrucciones)
        print(wrapp)
        print()
        x = int(input("Que deseas hacer?\n\t1. Estudiar\n\t2. Repasar\n\t3. Salir\n"))
        os.system('cls')

        if x == 1:
            Estudio.Est()

        elif x == 2:
            Repaso.Repa()

        elif x == 3:
            exit()

        else:
            print("No es una opcion valida\nPresiona Enter para continuar...")
            input()
            os.system('cls')

if __name__=="__main__":
    Oficialdecumplimiento()
