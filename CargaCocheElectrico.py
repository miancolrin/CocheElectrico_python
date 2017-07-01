# -*- coding: utf-8 -*-

#====================#
# EL COCHE ELÉCTRICO #
#    ES EL FUTURO    #
#====================#
# He credo este pequeño progrma en Python para hacer cáculos sobre el
# vehículo eléctrico, tales como cargas, autonomía y costes
# Este programa permite mediante un menú:
# =Calcular el tiempo de carga, tanto en AC como en DC
# =Cacular el precio de una carga completa
# =Calcular el coste de recorrer 100km
#
# Cualquier sugerencia o mejora de este programa será bien recibida
# Usad el código como queráis y para lo que queráis
#
# Creado por @miancolrin
#
# Versión en Python para Mac. Para la versión de Windows en C ir a
# https://github.com/miancolrin/CocheElectrico

import os
import math

def tiempoContinua():
    capacidad = int(input('Introduce capacidad de la batería en kWh: '))
    voltaje = int(input('Introduce voltaje de entrada: '))
    intensidad = int(input('Introduce intensidad de entrada: '))
    tiempo = capacidad / ((voltaje * intensidad) / 1000)
    print 'RESULTADO: El coche tarda en cargar', tiempo, 'horas'

def tiempoTrifasica():
    raizDeTres = math.sqrt(3)
    capacidad = int(input('Introduce capacidad de la batería en kWh: '))
    voltaje = int(input('Introduce voltaje de entrada: '))
    intensidad = int(input('Introduce intensidad de entrada: '))
    tiempo = capacidad / ((voltaje * intensidad * raizDeTres) / 1000)
    print 'RESULTADO: El coche tarda en cargar', tiempo, 'horas'

def precioCarga():
    capacidad = int(input('Introduce capacidad de la batería en kWh: '))
    precio = input('Introduce precio del kWh: ')
    coste = capacidad * precio
    print 'RESULTADO: El precio de una carga completa tiene un coste de', coste
    
def precioCien():
    media = input('Introduce la media de consumo (kW cada 100km): ')
    precio = input('Introduce precio del kWh: ')
    coste = media * precio
    print 'RSULTADO: El coste de recorrer 100km es de', coste

opc = 1
while opc != 0:
    os.system("clear")
    print '========================MENÚ========================'
    print '1. Tiempo de carga con corriente continua'
    print '2. Tiempo de carga con corriente alterna monofásica'
    print '3. Tiempo de carga con corriente alterna trifásica'
    print '4. Calcular precio de una carga completa'
    print '5. Calcular el coste de recorrer 100km'
    print '0. SALIR'
    opc = int(input('Opción: '))
    if opc == 1:
        os.system("clear")
        tiempoContinua()
        os.system( "read -n 1 -s -p \"Presione una tecla para continuar...\"" );
    elif opc == 2:
        os.system("clear")
        tiempoContinua()
        os.system( "read -n 1 -s -p \"Presione una tecla para continuar...\"" );
    elif opc == 3:
        os.system("clear")
        tiempoTrifasica()
        os.system( "read -n 1 -s -p \"Presione una tecla para continuar...\"" );
    elif opc == 4:
        os.system("clear")
        precioCarga()
        os.system( "read -n 1 -s -p \"Presione una tecla para continuar...\"" );
    elif opc == 5:
        os.system("clear")
        precioCien()
        os.system( "read -n 1 -s -p \"Presione una tecla para continuar...\"" );
