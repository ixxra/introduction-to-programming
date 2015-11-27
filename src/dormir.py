# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:03:53 2015

@author: usuario
"""

f = open('dormir.txt')
poema = f.read()
palabras = poema.split()

palabrasLargas = [palabra for palabra in palabras if len(palabra) > 3]


print 'Hay', len(palabrasLargas), 'en el poema'
print 'Sin repetir, hay', len(set(palabrasLargas)), 'palabras'

print 'Hay', len(set(palabras)), 'palabras sin repetir en el texto completo'