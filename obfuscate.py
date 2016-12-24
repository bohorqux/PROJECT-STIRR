#!/usr/bin/python

import sys
import random

uni_logic = {'P': ["!!P", "P || P", "P && P", "!!P && P", "!!P || P", "!!P && !!P", "!!P || !!P"]}

#We can express a single True or False value with any of the stored expressions
#As many times as we'd like, we could also recursivley go through a single value (i.e. P) and generate another equivalent expression based on our dictionary

def obfuscateBoolean(keys):
    #keys should never contain ')', '(', or certain keywords such as 'for' or 'if'. Implement data formatting to accomadate this in the future.
    #use enumeration with arrays to properly extract dictionary value. Should not hardcode 'P' below to return equivalent value.
    
    logic = random.choice(uni_logic['P']) #choose a random value that conserves logic, but appearence is altered.
    #Do not hardcode P, use enumeration to find indice of the single logic value and replace it with P in this instance.

    final = [keys[0], logic] + keys[1:] #We are assuming that our logic value comes right after the 'if' keyword
    return final

def main(argv):

    fileIn = open(argv[1], "r")

    for line in fileIn:
        if len(line) == 1:
            continue
        
        string = ""
        words = line.split()
        words = [x for x in words if x != ')' and x != '(']
        print("*** ", words)
        stirrd = obfuscateBoolean(words)
        print(stirrd)

    fileIn.close()
main(sys.argv)
