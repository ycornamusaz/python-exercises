#!/usr/bin/python3.4
# -*- coding: UTF-8 -*-

number = input('Entrez une température : ')
unit = input('Convertir vers des degrés (C)elsius ou (F)ahrenheit ? ')
if unit == "F" :
	output = (9.0/5.0)*float(number)+32
elif unit == "C" :
	output = (5.0/9.0)*(float(number)-32)
else :
	print('Veuillez entrer une unité correcte !')

print('Résultat : ' + str(round(float(output), 2)))

