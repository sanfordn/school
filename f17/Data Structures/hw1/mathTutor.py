"""
--------------------------------------------------
Name: Nick Sanford                               
File: mathTutor.py                            
Program Description: This program is designed to
    challenge students of grades 1, 2, and 3 in 
    various mathematic problems.                 
Date: 2 September 2017                           
--------------------------------------------------
"""

from random import randint

NUM_PROBLEMS = 5
rightAnswer = 0
wrongAnswer = 0

def main():
    print('Welcome to the Math Tutor')
    name = input('Enter your name: ')
    grade = getGrade()
    print('Hello,', name, 'and welcome to grade',grade,'mathematics.')
    mathTest(grade,name)
    writeToFile(grade,name)

def getGrade():
    while True:
        try:
            grade = int(input('Please enter your grade (1,2, or 3): '))
        except(ValueError):
            print('Sorry, not a valid grade. Please enter your grade using only (1,2, or 3): ')
            continue
        if grade < 1 or grade > 3:
            print('Sorry, not a valid grade. Please enter your grade using only (1,2, or 3): ')
        else:
            return grade
    #end while
"""Function that ensures the grade the user entered is valid, and returns the
    grade of the student as a usable value"""

def mathTest(grade,name):
    rightAnswer = 0
    wrongAnswer = 0
    for i in range(NUM_PROBLEMS):
        firstNum = generateNum(grade)
        secondNum = generateNum(grade)
        print('Problem #%s: ' %(i+1), str(firstNum))
        print('+'.rjust(12),str(secondNum))
        print('____'.rjust(16))
        answer = int(input('Answer:     '))
        check = checkAnswer(firstNum+secondNum,answer)
        if check == True:
            print('Great', name, 'your answer is correct!')
            rightAnswer+=1
        else:
            print('Sorry', name, 'your answer is incorrect. The correct answer is %s.'%(firstNum+secondNum))
            wrongAnswer+=1
    #endfor
"""Funciton takes in grade and name and creates a display and calls the
    function that generates the number. This function is used to actually test
    the students' math ability by piecing together other functions."""

def generateNum(grade):
    randNum = 0
    
    if grade == 1:
        randNum = randint(0,9)
    elif grade == 2:
        randNum = randint(10,99)
    else:
        randNum = randint(100,999)

    return randNum
"""Function takes in the student's grade number and generates numbers based
        on their grade"""

def checkAnswer(correct,attempt):
    return attempt == correct
"""Funciton used to check if the user's attempt at the problem is correct."""

def writeToFile(grade,name):
    f = open('Log.txt','a')
    f.write(' - User: %s in grade %s answered %s problems correctly, and %s problems incorrectly.\n'%(name,grade,rightAnswer,wrongAnswer))
    f.write('---------------------------------------------------------------------------------------------')
    f.close()

"""This function takes the grade and name of the student and writes a results
to a file, Log.txt"""

main()
