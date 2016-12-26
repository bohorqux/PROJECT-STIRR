#!/usr/bin/python

#Author: Xavier J. Bohorquez
#File: obfuscate.py
#Description: Consider this program a 'toolset' that contains the proper functions to obfuscate conditional statements and randomize the output of this obfuscation.

import sys
import random

#dictionary should be constructed as such -> {'P': ["!!P", "P || P", "P && P", "!!P && P", "!!P || P", "P", "!!P && !!P", "!!P || !!P"]}
#Assume P = True, or P = False. Every statement shown here must output to true

anti_bool = ["for", "while", "if", "||", "&&", "elif", "else", "!"]

#We can express a single True or False value with any of the stored expressions
#As many times as we'd like, we could also recursivley go through a single value (i.e. P) and generate another equivalent expression based on our dictionary

#-------------------------------------------------------------------------------------------------------------------------------------#
def createLogicDict(logicKey):
    """returns a dictionary containing equivalent logical expressions of the inputted logic key

       i-type:: string
       r-type:: dictionary
    """

    logicDict = {logicKey: ["!!" + logicKey, logicKey + " || " + logicKey, logicKey + " && " + logicKey,
                            "!!" + logicKey + " && " + logicKey, "!!" + logicKey + " || " + logicKey, logicKey,
                            "!!" + logicKey + " && " + "!!" + logicKey, "!!" + logicKey + " || " + "!!" + logicKey]
                 }

    return logicDict
#######################################################################################################################################
def obfuscateBoolean(key):
    """ Outputs equivalent boolean expression """

    logicDict = createLogicDict(key)
    
    logic = random.choice(logicDict[key]) #choose a random value that conserves logic, but appearence is altered.
    
    return logic
#########################################################################################################################################
def isTarget(elem):
    """Boolean function that returns true if the element inputted is a 'logic Key'.
       
       i-type:: string
       r-type:: boolean
    """
    if elem in anti_bool:
        return False
    else:
        return True
###########################################################################################################################################
def findAllP(source):
    """ returns array of len=2 tuples containing the indice of all logic elements stored in the source array 
    
        i-type:: array
        r-type:: (indice, item) IN array
    """

    reduced = []
    for index, item in enumerate(source):
        if isTarget(item):
            reduced += [(index, item)]
            
    return reduced
##############################################################################################################################################
def replaceSource(source, reduced):
    """replaces the key logic values in source with their alternative expression. Indices for these logic values are found in reduced array

       i-type:: array, (indice, item) IN array
       r-type:: array
    """

    for index, item in reduced:
        source[index] = obfuscateBoolean(item)

    return source
################################################################################################################################################

def main(argv):

    fileIn = open(argv[1], "r")

    for line in fileIn:
        if len(line) == 1:
            continue
        
        string = ""
        words = line.split()
        words = [x for x in words if x != ')' and x != '(']
        print("Original Case: ", words)
        logicKeys = findAllP(words)
        words = replaceSource(words, logicKeys)
        print("Obfuscated Case ", words)
        print()

    fileIn.close()
main(sys.argv)
