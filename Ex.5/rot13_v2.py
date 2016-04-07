#!/usr/bin/python3.4

import string

def to_rot13(dat_in) :
    maj_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    min_chars = "abcdefghijklmnopqrstuvwxyz"
    dat_out = ""

    # Analise and replace MAJ chars
    z = int(0)

    # Select char[n] from the input
    for a in dat_in :
        y = int(0)
        base_placement = -1
        placement = 0

        # Select char[n] from maj_chars (base)
        while (y < 27) :
            if (y < 26) :
                base_placement = int(dat_in[z].find(maj_chars[y]))

                # Compare input and base char
                if (base_placement != -1) :

                    # Shift char of 13
                    placement = y + 13
    
                    # If char is out of alphabet, subtract 26 and add char to output
                    if placement > 26 :
                        placement = placement - 26
                        dat_out = dat_out + maj_chars[placement]
                        break
    
                    # If not, add char to output
                    else :
                        dat_out = dat_out + maj_chars[placement]
                        break
    
            # If the char in not reconise, add it to output
            else :

                # Select char[n] from the input
                w = int(0)
                base_placement = -1
                placement = 0
    
                # Select char[n] from min_chars (base)
                while (w < 27) :
                    if (w < 26) :
                        base_placement = int(dat_in[z].find(min_chars[w]))
        
                        # Compare input and base char
                        if (base_placement != -1) :
        
                            # Shift char of 13
                            placement = w + 13
        
                            # If char is out of alphabet, subtract 26 and add char to output
                            if placement > 26 :
                                placement = placement - 26
                                dat_out = dat_out + min_chars[placement]
                                break
        
                            # If not, add char to output
                            else :
                                dat_out = dat_out + min_chars[placement]
                                break
        
                    # If the char in not reconise, add it to output
                    else :
                        dat_out = dat_out + dat_in[z]
                    w = w + 1

            y = y + 1
        z = z + 1
    return dat_out

while True :
    
    dat_input = input(" -> ")
    if dat_input == "" :
        exit()
    dat_output = to_rot13(dat_input)
    print(dat_output)

           
