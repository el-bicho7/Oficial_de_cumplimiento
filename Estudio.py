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

calificacion = { 1 : 0,
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
                 13: 0}

while True:
    print("------------------------------------------------------")
    print("Que deseas praticar? (Solo opciones disponibles)\n\t1. 40 Recomendaciones\t\t\t", calificacion[1],"%\n\t2. Leyes\t\t\t\t", calificacion[2],"%\n\t3. Clientes y Usuarios\t\t\t", calificacion[3],"%\n"
          "\t4. Regimen Simplificado\t\t\t", calificacion[4], "%\n\t5. Plazos Regularios\t\t\t", calificacion[5], "%\n\t6. Umbrales de identificacion\t\t", calificacion[6],"%\n"
          "\t7. Lineamientos de la auditoria\t\t", calificacion[7], "%\n\t8. Infracciones\t\t\t\t", calificacion[8], "%\n\t9. Auditoria\t\t\t\t", calificacion[9], "%\n"
          "\t10. Sistema automatizado, OC y CCC\t", calificacion[10],"%\n\t11. Guia EBR para el sector bancario\t", calificacion[11],"%\n\t12. Adecuada gestion del riesgo\t\t", calificacion[12],"%\n"
          "\t13. Obligaciones\t\t\t", calificacion[13],"%\n\t0. Salir\n")
    #print(f"calificacion = {calificacion}") #f-string 
    n = int(input())
    os.system('cls')
    if n == 1:
        calificacion[1] = Recomendaciones40.Recomendaciones()
        
    elif n == 2:
        calificacion[2] = Leyes.Leyes()

    elif n == 3:
        calificacion[3] = ClientesUsuarios.clientesyusuarios()

    elif n == 4:
        calificacion[4] = RegimenSimp.Regimen_sim()

    elif n == 5:
        calificacion[5] = Plazos.plazos()

    elif n == 6:
        calificacion[6] = Niveles.niveles()

    elif n == 7:
        calificacion[7] = LineamientosAuditoria.lin_auditoria()

    elif n == 8:
        calificacion[8] = Infracciones.sanciones()
        
    elif n== 9:
        calificacion[9] = Auditoria.auditoria()

    elif n== 10:
        calificacion[10] = CCCyOC.funciones()

    elif n== 11:
        calificacion[11] = Guia_EBR.guia()

    elif n== 12:
        calificacion[12] = Adecuada_gestion.elementos()

    elif n== 13:
        calificacion[13] = Obligaciones.obligaciones()
        
    elif n == 0:
        exit()

    
