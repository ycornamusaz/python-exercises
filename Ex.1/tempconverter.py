#!/usr/bin/python3.4
# -*- coding: UTF-8 -*-

import sys

if len(sys.argv) != 3 :
    number = input('Entrez une température : ')
    unit = input('Convertir vers des degrés (C)elsius ou (F)ahrenheit ? ')
else :
    number = sys.argv[1]
    unit = sys.argv[2]


if unit == "F" :
    output = (9.0/5.0)*float(number)+32
elif unit == "C" :
    output = (5.0/9.0)*(float(number)-32)
else :
    print('Veuillez entrer une unité correcte !')

print('Résultat : ' + str(round(float(output), 2)))

