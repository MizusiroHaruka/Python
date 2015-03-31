# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if secretWord=='':
        return True
    else:
        return secretWord[0] in lettersGuessed and isWordGuessed(secretWord[1:], lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    if secretWord=='':
        return ''
    else:
        if secretWord[0] in lettersGuessed:
            return secretWord[0]+getGuessedWord(secretWord[1:], lettersGuessed)
        else:
            return '_ '+getGuessedWord(secretWord[1:], lettersGuessed)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    a=''
    import string
    for i in string.ascii_lowercase:
        if not (i in lettersGuessed):
            a+=i
    return a

def hangman(secretWord):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+ ' letters long.')
    mistakesMade=0
    lettersGuessed=[]
    while 8-mistakesMade>0:
        print('-----------')
        print('You have '+str(8-mistakesMade)+' guesses left.')
        print('Available letters: '+getAvailableLetters(lettersGuessed))
        le=raw_input('Please guess a letter: ')
        if not('a'<=le and le<='z' or 'A'<=le and le<='Z'):
            raise Exception('Wrong input')
        le=le.lower()
        if le in lettersGuessed:
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(le)
            if le in secretWord:
                print('Good guess: '+getGuessedWord(secretWord, lettersGuessed))
            else:
                print('Oops! That letter is not in my word: '+getGuessedWord(secretWord, lettersGuessed))
                mistakesMade+=1
        if isWordGuessed(secretWord, lettersGuessed):
            break
    print('-----------')                
    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was else.')

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'c'
hangman(secretWord)
