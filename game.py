import secrets
import random
import math

optionWordsToGuess = ['cat', 'dog', 'rabbit', 'wolf', 'horse', 'cow', 'elephant', 'bird', 'fox', 'tiger', 'lion', 'giraffe', 'zebra', 'panda', 'koala', 'cheetah', 'rhinoceros', 'hippopotamus', 'kangaroo', 'alligator']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def setWordToGuess(optionWordsToGuess):
    wordToGuess = secrets.choice(optionWordsToGuess)
    wordToGuessLetters = list(wordToGuess)
    return wordToGuess, wordToGuessLetters


def getWordToGuessLetterIndices(wordToGuess, wordToGuessLetters, alphabet):
    letterPositionInAlphabet = []

    for letter in wordToGuess:

        actualPosition = 0
        letterPositionInAlphabetReached = False

        while not letterPositionInAlphabetReached:
            if alphabet[actualPosition] == letter:
                letterPositionInAlphabetReached = True
                letterPositionInAlphabet.append(actualPosition)
            else:
                actualPosition += 1
    return letterPositionInAlphabet


def hideLettersWordToGuess():
    wordToGuessAmountOfLettersHidden = 0
    actualPosition = 0
    wordToGuessGame = ''
    wordToGuessHiddenLettersPercent = math.floor(len(wordToGuess) * (60/100))
    letterPositionInAlphabetReached = False
    gameLetterAddedFromAlphabet = [0]* len(alphabet)

    while wordToGuessAmountOfLettersHidden < wordToGuessHiddenLettersPercent:
        for letter in range (0, len(wordToGuess)):

            hideAPosition = random.randint(0,1)
            
            if hideAPosition == 1:
                wordToGuessAmountOfLettersHidden +=1
                wordToGuessGame += ' _ '
            else:
                actualPosition = 0
                wordToGuessGame += wordToGuessLetters[letter]
                while not letterPositionInAlphabetReached:
                    if alphabet[actualPosition] == wordToGuessLetters[letter]:
                        letterPositionInAlphabetReached = True
                        gameLetterAddedFromAlphabet[actualPosition] = 1
                    actualPosition += 1
    return gameLetterAddedFromAlphabet

    
def getPlayerInput(letterPositionInAlphabet, gameLetterAddedFromAlphabet):
    amountOfAttempts = 10
    wordGuessed = False

    while amountOfAttempts >= 0:

        wordToGuessGame = ''

        for letterPosition in range (0, len(letterPositionInAlphabet)):
            if gameLetterAddedFromAlphabet[letterPositionInAlphabet[letterPosition]] == 1:
                wordToGuessGame += alphabet[letterPositionInAlphabet[letterPosition]] + ' '
            else:
                wordToGuessGame += '_ '
                
        if '_' not in wordToGuessGame:
            print(f"You won the game! The word was '{wordToGuess}'")
            wordGuessed = True
            break
        else:
            letterOrWord = input(f'Write a letter or a word for {wordToGuessGame}. Attemps: {amountOfAttempts}')
            letterOrWord.lower()
            letterOrWordArray = list(letterOrWord)

            for letter in letterOrWordArray:
                if letter in alphabet:
                    #Add error when the player don't input a lowercase letter of the alphabet (uppercase, symbols)
                    amountOfAttempts -= 1
                    if len(letterOrWord) > 1:
                        if letterOrWord == wordToGuess:
                            print(f"You won the game! The word was '{wordToGuess}'")
                            wordGuessed = True
                            break
                        else:
                            print("You don't guess the word")

                    else:
                #Replace 0 to 1 in the letter
                        amountOfLettersAdded = 0
                        actualPosition = 0
                        letterPositionInAlphabetReached = False

                        while amountOfLettersAdded != len(wordToGuess):
                            amountOfLettersAdded += 1
                            while not letterPositionInAlphabetReached:
                                for letter in alphabet:
                                    if letterOrWord == letter:
                                        letterPositionInAlphabetReached = True
                                        break
                                    actualPosition += 1
                        gameLetterAddedFromAlphabet[actualPosition] = 1
                else:
                    print("You must type characters of the alphabet. Try again")

            if amountOfAttempts == 0 and not wordGuessed:
                print(f"You lost :( There's no more attempts. The word was '{wordToGuess}")


wordToGuess, wordToGuessLetters = setWordToGuess(optionWordsToGuess)
letterPositionInAlphabet = getWordToGuessLetterIndices(wordToGuess, wordToGuessLetters, alphabet)
gameLetterAddedFromAlphabet = hideLettersWordToGuess()
getPlayerInput(letterPositionInAlphabet, gameLetterAddedFromAlphabet)