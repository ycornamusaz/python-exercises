#!/usr/bin/python

import string
import sys

if len(sys.argv) != 2 :
    exit()
else :
    filename = sys.argv[1]

txt = open(filename)
print(filter(lambda x: x in string.printable, txt.read()))
