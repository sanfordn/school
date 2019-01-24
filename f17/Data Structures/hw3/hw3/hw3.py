"""
Name: Nick Sanford
Program: hw3.py
Description: A simple text-editor program that
    utilizes your CursorBasedList class.
Date: 7 October 2017
"""
from cursor_based_list import CursorBasedList
from os.path import exists
NEWL= "\n"

def main():
    print('Welcome to Text edior')
    print('\n=================================================================\n')
    fileName = input("\nPlease enter the name of the .txt file you would like to edit. ")
    myFile = openFile(fileName)
    myList = file2List(myFile)
    while True:
        print('\n=================================================================\n')
        choice = updateInfo(myList)
        if choice == 'A' or choice == 'a':
            """Insert new line after current line"""
            after(myList)
        elif choice == 'B' or choice == 'b':
            """Insert new line before current line"""
            print(choice)
            before(myList)
        elif choice == 'F' or choice == 'f':
            """Change current to first"""
            myList.first()
        elif choice == 'L' or choice == 'l':
            """Change current to last"""
            myList.last()
        elif choice == 'N' or choice == 'n':
            """Change current to next line"""
            nextLine(myList)
        elif choice == 'P' or choice == 'p':
            """Change current to previous line"""
            previousLine(myList)
        elif choice == 'R' or choice == 'r':
            """Remove current line"""
            if myList.isEmpty():
                print("No lines to remove from an empty file...")
            else:
                print("Removed",myList.getCurrent(),"from file.\n")
                myList.remove()
        elif choice == 'U' or choice == 'u':
            """Replace current line"""
            replaceLine(myList)
        elif choice == 'X' or choice == 'x':
            """Save list, rewrite, and exit"""
            save(myList,fileName)
            break
        elif choice == 'C' or choice == 'c':
            """Copy and paste a line"""
            copyPaste(myList)
            
        elif choice == 'W' or choice == 'w':
            """Find word and find next occurance"""
            findWord(myList)
            
        elif choice == 'D' or choice == 'd':
            """Replace a specified word/string by another word/string"""
            findReplaceWord(myList)
        else:
            print("Invalid menu choice!")
            
def copyPaste(myList):
    copy = myList.getCurrent()
    

def findWord(myList):
    pass
    
def findReplaceWord(myList):
    pass
  
def after(myList):
    """Precondition:
    Postcondition: new line is inserted after current line, and updated to the
        current line"""
    newLine = input("Enter a new line of text:\n")
    myList.insertAfter(NEWL + newLine)
    
def before(myList):
    """Precondition: 

    Postcondition: new line is inserted before the current line, and updated to the
        current line"""
    newLine = input("Enter a new line of text:\n")
    myList.insertBefore(NEWL + newLine)
    
def nextLine(myList):
    """Precondition: there is more than one line in the list

       Postcondition: current line is updated to the next line"""
    if myList.hasNext():
        myList.next()
    else:
        print("There is no next line!")
        
def previousLine(myList):
    """Precondition: there is more than one line in the list

       Postcondition: current line is updated to the next line"""
    if myList.hasPrevious():
        myList.previous()
    else:
        print("There is no previous line!")
        
def replaceLine(myList):
    """Precondition: list is not empty

       Postcondition: replace current line with a new line the user creates"""
    if myList.isEmpty():
        print("no line to replace in an empty list...")
    else:
        newLine = input("Enter the line of text you would like to replace",myList.getCurrent(),"with: ")
        print("Replaced",myList.getCurrent(),"with",newLine)
        myList.replace(newLine)
    
def save(myList,fileName):
    """Precondition: list is not empty

       Postcondition: list is written to file"""
    myFile = open(fileName,'w')
    if myList.isEmpty():
        myFile.write('')
    else:
        myList.first()
        myFile.write(myList.getCurrent())
        while myList.hasNext():
            myList.next()
            myFile.write(myList.getCurrent())
        

def updateInfo(myList):
    """Precondition:

       Postcondition: prints out the list and gives user options in the menu"""
    print("Number of lines in file:",len(myList))
    if myList.isEmpty():
        print("\nEmpty List...")
    else:
        print("\nCurrent text in file:\n%s" %myList)
        print('\nCurrent line =',myList.getCurrent())
    print('\nMenu: ')
    print("A - insert line After")
    print("B - insert line Before")
    print("F - edit First line")
    print("L - edit Last line")
    print("N - edit Next line")
    print("P - edit Previous line")
    print("R - remove line")
    print("U - replace line")
    print("X - eXit and save file")
    choice = input("Menu Choice? ")
    return choice

def file2List(myFile):
    """Precondition:

       Postcondition: takes each line in file and creates a new node one after another"""
    myList = CursorBasedList()
    for line in myFile:
        myList.insertAfter(line)
    
    myFile.close()
    return myList

def openFile(fileName):
    """Precondition: file exists

       Postcondition: takes name of text file, finds it, and opens it to be readable"""
    while not exists(fileName):
        print("Sorry, file", fileName, "does NOT exist! --- Please try again!")
        fileName = input("Enter file name (e.g., aTextFile.txt): ")
    # Open the file for reading 'r'
    myFile = open(fileName, 'r')
    return myFile

main()
