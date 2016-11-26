#!/usr/bin/python3

#formatted assuming that brackets appear on their own lines
def formatThis(filename, tabbing, newLining):
    """Function used to format source code to implement the specified
       amount of tabs and spaces.

       filename: 
               type -> readable file
               desc.-> name of file that will undergo the specified formatting.
       tabbing:
               type -> string
               desc.-> when necessary tabbing occurs, add this string to tab. ex. "\t"
       newLining:
               type -> string
               desc.-> when newLine must occur, use this string to act as new line. "\n"
     """
    
    fileIn = open(filename, "r")
    fileOut = open("stirr.c", "w")

    tabCount = 0
    
    for line in fileIn:
        tabbed = tabbing * tabCount
        setLine = tabbed + line
        
        if "{" in setLine:
            fileOut.write(setLine)
            tabCount += 1

        elif "}" in setLine:
            fileOut.write(setLine)
            tabCount -= 1
        else:
            fileOut.write(setLine)
            
        fileOut.write(newLining)

    fileOut.close()
    fileIn.close()
    
