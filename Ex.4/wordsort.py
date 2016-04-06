#!/usr/bin/python3.4

import sys
import re
from collections import Counter

if len(sys.argv) != 2 :
    print("Please specify an argument !")
    print("wordsort.py <file>")
    exit()
else :
    filename = sys.argv[1]
    txt = open(filename,"r",1)
    texte = txt.read()
    listeword = re.findall('\w+', texte)
    dico = dict(Counter(listeword))
    no_duplicate = list(set(listeword))
    for w in no_duplicate:
        print(w + " : " + str(dico[w]))
