#Exercise 13.1. Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.

import sys
import string

def stringManipulation(file):
    '''
    Tokenizes a set of text into each word, removing punctuation and making lowercase
    Returns an array with all instances of words
    '''
	
    file = open(file)
    modifiedWords = []    #variable used to store all of the stripped tokens
    for line in file.readlines():
        cleanedLine = line.strip()  #remove whitespace
        words = cleanedLine.split()  #split each line into a list of individual strings
        for word in words:
            word = word.translate(string.maketrans("",""), string.punctuation).lower() #remove punctuation and convert to lowercase,
            modifiedWords = modifiedWords + [word]  #concat arrays to create one big array of all words
    return modifiedWords    #return array of all words
def main():  
    print stringManipulation('file.txt')
    return 0
if __name__ == "__main__":
    main()
