# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:03:53 2015

@author: usuario
"""

f = open('dormir.txt')
poema = f.read()
palabras = poema.split()

palabras_sin_repetir = set(palabras)

histograma = {} #Diccionario vacio

for palabra in palabras_sin_repetir:
    histograma[palabra] = palabras.count(palabra)


#histograma = {palabra:palabras.count(palabra) for palabra in palabras_sin_repetir}
    
import json
datos = json.dumps(histograma)

print datos  