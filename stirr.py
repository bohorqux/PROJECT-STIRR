#!/usr/bin/python3

import sys
from formatter import *

##############################

#FUNCTIONS

def switchHalfs(s):
    """type: string
       rtype: string
       returns the original string, switching the placement
       of both halfs.
                     """
    
    middle = len(s)//2
    s1 = s[0:middle]
    s2 = s[middle:]
    switched = s2 + s1
    return switched

def altOperator(arg1, op, arg2):
    
    if op == ">=":
        s1 = arg1 + " > " + arg2
        s2 = arg1 + " == " + arg2
        s_all = s1 + " || " + s2
        return s_all.split()

    elif op == "<=":
        s1 = arg1 + " < " + arg2
        s2 = arg1 + " == " + arg2
        s_all = s1 + " || " + s2
        return s_all.split()
        
    elif op == ">":
        stirrd = arg2 + " < " + arg1
        return stirrd.split()

    elif op == "<":
        stirrd = arg2 + " > " + arg1
        return stirrd.split()

def altIterator(fi, fo, contents):

    if contents[0] == "for":
        fo.write("%s = %s\n" % (contents[2], contents[4]))
        fo.write("while ( %s %s %s )\n" % (contents[5], contents[6], contents[7][0:-1]))
        
    for line in fi:
        if "}" in line:
            fo.write("%s;\n" % contents[-2])
            fo.write("}")
            return
        else:
            fo.write(line)
                
##############################

#PRE-EXECUTION: Error Checking

def pre_errorCheck(argv):
    """ type: void
        rtype: void
        function that makes all necessary error checks before
        execution """
    
    if len(argv) != 2:
        print("Invalid number of arguments. Please enter as shown:\n$ ./stirr.py [source code]")
        return False

    return True

###############################

def main(argv):
    
    if pre_errorCheck(argv) == False:
        return 0
    
    fileIn = open(argv[1], "r")
    fileOut = open("pre_stirr.c", "w")

    for line in fileIn:
        outLine = ""
        data = line

        if len(data) == 1:
            continue
        
        words = data.split()

        if "if" in words:
            print("CONDITION KEYWORD FOUND!")
            print("Obfuscating line...")
            newLine = altOperator(words[2], words[3], words[4])
            words = [words[0], words[1]] + newLine + [words[5]]

        if "for" in words:
            altIterator(fileIn, fileOut, words)
            continue
        
        for wrd in words:
            outLine += wrd + " "

        fileOut.write(outLine)
        fileOut.write("\n")

    fileIn.close()
    fileOut.close()

    formatThis("pre_stirr.c", "   ", "\n")
    
if __name__ == "__main__":
    main(sys.argv)
    
