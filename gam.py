import secrets
import random
import math

optionWordsToGuess = ['cat', 'dog', 'rabbit', 'wolf', 'horse', 'cow', 'elephant', 'bird', 'fox', 'tiger', 'lion', 'giraffe', 'zebra', 'panda', 'koala', 'cheetah', 'rhinoceros', 'hippopotamus', 'kangaroo', 'alligator']
wordToGuess = secrets.choice(optionWordsToGuess)
wordToGuessLetters = list(wordToGuess)
wordToGuessUniqueLetters = set(wordToGuessLetters)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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

amountOfAttempts = 10

while amountOfAttempts > 0:

    wordToGuessGame = ''

    for letterPosition in range (0, len(letterPositionInAlphabet)):
        if gameLetterAddedFromAlphabet[letterPositionInAlphabet[letterPosition]] == 1:
            wordToGuessGame += alphabet[letterPositionInAlphabet[letterPosition]] + ' '
        else:
            wordToGuessGame += '_ '
            
    if '_' not in wordToGuessGame:
        print(f"You won the game! The word was '{wordToGuess}'")
        break
    else:
        letterOrWord = input(f'Write a letter or a word for {wordToGuessGame}. Attemps: {amountOfAttempts}')
        amountOfAttempts -= 1
        if len(letterOrWord) > 1:
            if letterOrWord == wordToGuess:
                print(f"You won the game! The word was '{wordToGuess}'")
                break  # CAMBIO: Se agrega break para salir del bucle si adivinan la palabra.
            else:
                print("You don't guess the word")
                # CAMBIO: Ahora, después de no adivinar la palabra, el bucle continúa solicitando más letras/palabras.
        else:
            actualPosition = 0
            letterPositionInAlphabetReached = False
            while not letterPositionInAlphabetReached and actualPosition < len(alphabet):
                if alphabet[actualPosition] == letterOrWord:
                    letterPositionInAlphabetReached = True
                    gameLetterAddedFromAlphabet[actualPosition] = 1
                actualPosition += 1  # CAMBIO: Este bloque se usa para procesar la letra ingresada.

if amountOfAttempts == 0:
    print("You lost :( There's no more attempts")  # CAMBIO: Corrección en la palabra "attempts"
