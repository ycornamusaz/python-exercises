#!/usr/bin/python

from random import randint
to_guess = randint(0,100)
guessed = input ("Entrez un nombre (entre 0 et 100)(faille : to_guess): ")
if guessed == to_guess :
    print "Gagne !"
else :
    print "Perdu !"
