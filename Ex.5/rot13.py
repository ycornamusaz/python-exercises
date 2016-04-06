#!/usr/bin/python3.4

import codecs


while True :

    dat_input = input(" -> ")
    if dat_input == "" :
        exit()
    dat_output = codecs.encode(dat_input, 'rot13')
    print(dat_output)
    
