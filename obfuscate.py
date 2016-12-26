#!/usr/bin/python

import sys
import random

uni_logic = {'P': ["!!P", "P || P", "P && P", "!!P && P", "!!P || P", "!!P && !!P", "!!P || !!P"]}
anti_bool = ["for", "while", "if", "||", "&&", "elif", "else", "!"]

#We can express a single True or False value with any of the stored expressions
#As many times as we'd like, we could also recursivley go through a single value (i.e. P) and generate another equivalent expression based on our dictionary

def obfuscateBoolean(key):
    """ Outputs equivalent boolean expression """
    
    logic = random.choice(uni_logic[key]) #choose a random value that conserves logic, but appearence is altered.
    
    return logic

def findP(keys):
    """ Function that obtains single boolean expression based on given array of values
        itype: array
        rtype: indice
    """

    for index, item in enumerate(keys):
        if item not in anti_bool:
            return index
    return -1

def main(argv):

    fileIn = open(argv[1], "r")

    for line in fileIn:
        if len(line) == 1:
            continue
        
        string = ""
        words = line.split()
        words = [x for x in words if x != ')' and x != '(']
        print("*** ", words)
        p_Indice = findP(words)
        words[p_Indice] = obfuscateBoolean(words[p_Indice])
        print(words)

    fileIn.close()
main(sys.argv)
