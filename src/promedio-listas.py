# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:05:07 2015

@author: usuario

Promedio de los datos, utilizando listas
"""


datos = []

numero = raw_input("Ingresa un dato: ")
numero = float(numero)

while numero != 0:
    datos.append(numero)
    numero = raw_input("Ingresa un dato: ")
    numero = float(numero)


if len(datos) > 0:
    print "Promedio:", sum(datos)/len(datos)    
    print "Max:", max(datos)
    print "Min:", min(datos)
else:
    print "Sin datos"