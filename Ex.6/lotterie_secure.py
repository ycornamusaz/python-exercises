#!/usr/bin/python

from random import randint
guessed = input ("Entrez un nombre (entre 0 et 100): ")
if guessed == randint(0,100) :
    print "Gagne !"
else :
    print "Perdu !"
