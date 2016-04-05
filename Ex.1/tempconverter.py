#!/usr/bin/python3.4
# -*- coding: UTF-8 -*-

import sys

# Check if arguments are present
if len(sys.argv) != 3 :
    # If no, question
    number = float(input('Entrez une température : '))
    unit = input('Convertir vers des degrés (C)elsius ou (F)ahrenheit ? ')
else :
    # If yes, use arguments
    number = float(sys.argv[1])
    unit = sys.argv[2]

# Check conversion type and calcul
if unit == "F" :
    output = (9.0/5.0)*number+32
elif unit == "C" :
    output = (5.0/9.0)*(number-32)
else :
    # If conversion type isn't correct, dispay an error
    print('Veuillez entrer une unité correcte !')
    exit()
i
# Print result
print('Résultat : ' + str(round(float(output), 2)))

