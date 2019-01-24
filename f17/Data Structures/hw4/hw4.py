"""

"""

from chaining_dictionary import ChainingDict
from time import clock

def main():
    movieFile = open('movieData.txt', 'r', encoding='utf8')
    movieDict = ChainingDict(40000)
    movieStr = movieFile.read()
    movies = movieStr.split('/n')
    wordList = movieStr.split()

    print(movies)
    
main()
