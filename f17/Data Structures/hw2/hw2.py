"""
Name: Nick Sanford
Date: 9 Sept 2017
File Name: hw2.py
File Description: This program is used to encrypt any message given in a .txt file, and then
    write it to a .zzz file. It uses a legend given by ENCRYPT_STRING in which it has every
    character needed to say something in the english language. This encryption method uses a
    key and cypher (ENCRYPTED_STRING) to encrypt and decrypt the messages by shifting indexes
    on characters by the amount given in a key.
"""
from os.path import exists

ENCRYPT_STRING = 'aA0bB1cC2dD3eE4fF5gG6hH7iI8jJ9kK lL,mM.nN?oO/pP;qQ:rR\'sS\"tT!uU@vV$wW%xX&yY-zZ='
ENCRYPT_LIST = list(ENCRYPT_STRING)
def main():
    print('Welcome to the Encryption/Decryption Program')
    xit = False
    while xit == False:
        validStrings = ['e', 'd', 'x']
        choice = input('Would you like to:\n(e)ncrypt a file\n(d)ecrypt a file\ne(x)it\n(enter e, d, or x)?: ')
        while choice not in validStrings:
            choice = input("Sorry, that’s an invalid choice. Please enter only e, d, or x: ")
        if choice == validStrings[0]:
            encryptFile()
        elif choice == validStrings[1]:
            decryptFile()
        else:
            xit = True
    
    print('Bye!')
"""
EncryptFile()
This function is the main file that encrypts the message in a .txt and writes it to a .zzz file
"""
def encryptFile():
    origKey = validKey()
    key = origKey
    fileName = input("Enter file name of the message you would like to encrypt (e.g., aTextFile.txt): ")
    stringOfFile = findFile(fileName)
    strWrite = ''
    for ch in stringOfFile:
        valid = checkCharValid(ch)
        if valid:
            (newChar,key) = encryptChar(ch,key)
            strWrite +=newChar

    newFileName = writeEncrypt(strWrite)
    print("The file '",fileName,"' was successfully encrypted using a key of",origKey,"to the file'",newFileName,"'")
"""
DecryptFile()
This function is the main file use that encrpts a message in a .zzz file and writes it to a .txt file
"""
def decryptFile():
    origKey = validKey()
    key = origKey
    fileName = input("Enter a file name of the encrypted message you would like to decrypt (e.g., aTextFile.zzz): ")
    stringOfFile = findFile(fileName)
    strWrite = ''
    for ch in stringOfFile:
        valid = checkCharValid(ch)
        if valid:
            (newChar,key) = decryptChar(ch,key)
            strWrite += newChar
    newFileName = writeDecrypt(strWrite)
    print("The file '",fileName,"' was successfully decrypted using a key of",origKey,"to the file'",newFileName,"'")
    
"""
writeDecrypt()
This function is used to check if the file already exists and see if user wants to write in a different file
    or overwrite this file. This file takes in the decrypted string and writes it to a file and then returns the
    file name to a the calling function
"""

def writeDecrypt(message):
    fileName = 'message.txt'
    if exists(fileName):
        okay = input("WARNING: The file '%s' already exists!\nIs it okay to wipe it out (y/n): "%fileName)
        if okay == 'n':
            fileName = input('Enter the file name that should be used (.txt extention will automatically be added): ')
            fileName += '.txt'
    myFile = open(fileName,'w')
    myFile.write(message)
    return fileName

"""
writeEncrypt()
This function is used to check if the file already exists and see if user wants to write in a different file
    or overwrite this file. This file takes in the decrypted string and writes it to a file and then returns the
    file name to a the calling function
"""
def writeEncrypt(message):
    fileName = 'message.zzz'
    if exists(fileName):
        okay = input("WARNING: The file '%s' already exists!\nIs it okay to wipe it out (y/n): "%fileName)
        if okay == 'n':
            fileName = input('Enter the file name that should be used (.zzz extention will automatically be added): ')
            fileName += '.zzz'
    myFile = open(fileName,'w')
    myFile.write(message)
    return fileName

"""
findFile()
This function is used to ensure the file the user is wanting to encrypt or decrypt exists.
    It continually asks the user for the name of the file until it finds an existing file.
    This file gets the file name, opens up the file, and then reads in the file as a string
    and sends it to another function. 
"""
def findFile(fileName):
    while not exists(fileName):
        print("Sorry, file", fileName, "does NOT exist! --- Please try again!")
        fileName = input("Enter file name to split into words (e.g., aTextFile.txt): ")

    # Open the file for reading 'r'
    myFile = open(fileName, 'r')
    # read whole file into a single string!
    stringOfFile = myFile.read()
    return stringOfFile

"""
encryptChar()
This function is the main function used to encrypt the current character. It takes in
    the current character and key and returns the decrypted one by shifting the index
    by whatever the key is. This also returns the next key.
"""
def encryptChar(ch,key):
    normIndex = ENCRYPT_LIST.index(ch)
    encryptIndex = checkIndex(ENCRYPT_LIST.index(ch) + key)
    nextKey = correctIndex(normIndex)
    encryptedCh = ENCRYPT_LIST[encryptIndex]
    return encryptedCh,nextKey
"""
decryptChar()
This function is the main function used to read in the current character and decrypt it
    based on our key. it takes in a character and the current key and it returns the
    decrypted character and the next key.
"""
def decryptChar(ch,key):
    normIndex = ENCRYPT_LIST.index(ch)
    decryptIndex = checkIndex(ENCRYPT_LIST.index(ch) - key)
    nextKey = correctIndex(decryptIndex)
    decryptedCh = ENCRYPT_LIST[decryptIndex]
    return decryptedCh,nextKey

"""
checkIndex()
This function ensures that the index we are using is between 0 and 77 and helps the
    indexing 'loop around' back to zero or 78 depending which way the key is moving.
"""
def checkIndex(index):
    if index > 77:
        return index-78
    elif index <0:
        return index+78
    else:
        return index

"""
validKey()
This function ensures that the user inputs a valid original key (any positive integer) so we can
    encrypt/decrypt based on that key.
"""
def validKey():
    while True:
        try:
            key = int(input('What positive integer key would you like to use for encryption/decryption?: '))
            if key <0:
                print('Sorry, that’s an invalid choice. Please enter a positive integer')
            else:
                return key
        except:
            print('Sorry, that’s an invalid choice. Please enter a positive integer')
"""
correctIndex()
This function is used to correct the index value used in encrypting or decrypting a char. It takes in the original
    index, and decrypts it depending on what interval of numbers it is in. For example, if an index is
    taken in between 30 and 40, let's say 34, then this function subtracts 30 from the number, and it uses
    the key of 4 to be added to the index to find where the next char is.
"""           
def correctIndex(index):
    if index < 10:
        return index
    elif index >=10 and index < 20:
        return index-10
    elif index >=20 and index < 30:
        return index-20
    elif index >=30 and index < 40:
        return index-30
    elif index >=40 and index < 50:
        return index-40
    elif index >=50 and index < 60:
        return index-50
    elif index >=60 and index < 70:
        return index-60
    elif index >=70 and index <=77:
        return index-70
"""
chechCharValid()
This function is used to validate the current character to ensure it is within the list of
    characters we are allowed to encrypt/decrypt based on the original legend/cypher we are
    given.
"""
def checkCharValid(ch):
    if ch not in ENCRYPT_LIST:
        return False
    else:
        return True

main()
