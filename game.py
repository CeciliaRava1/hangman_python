#variables
import secrets
import random
import math
word_letters = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
position_letter = [0]* len(alphabet)
list = ['cat', 'dog', 'rabbit', 'wolf', 'horse', 'cow', 'elephant', 'bird', 'fox']
word = secrets.choice(list)
word_game = ''
word_lenght = len(word)
position_word = []
reached = 0
position = 0
counter = 0
attemps = 3
jupiter = []

#Discover letters of the word without repetition
times = 0
number = 0
caracter = word[0]
word_letters.append(word[0])
for i in range (0, len(word)-1):
    number += 1
    if caracter != word[number]:
        word_letters.append(word[number])

#Vector with letters of the word
for i in word:
    jupiter.append(i)

#Position numbers of words in the alphabet
for i in word:
    reached = 0
    position = 0
    while reached != 1:
        if alphabet[position] == i:
            reached = 1
            position_word.append(position)
        else:
            position += 1

#Hide letters
hidden = 0
coso = ''
position = 0
print(word)
hide_percent = math.floor(word_lenght * (60/100))
while hidden < hide_percent:
    for i in range (0, len(word)):
        random_number = random.randint(0,1)
        if random_number == 1:
            hidden +=1
            word_game += ' _ '
        else:
            reached = 0
            position = 0
            word_game += jupiter[i]
            while reached != 1:
                if alphabet[position] == jupiter[i]:
                    reached = 1
                    position_letter[position] = 1
                position += 1

#Input word or letter
while attemps > 0:
    palabra = ''
    #Print new word
    for i in range (0, len(position_word)):
        if position_letter[position_word[i]] == 1:
            palabra += alphabet[position_word[i]] + ' '
        else:
            palabra += '_ '
            
    if '_' not in palabra:
        print('you won')
        break
    else:
        letter = input(f'Write a letter or a word for {palabra}. Attemps: {attemps}')
        attemps -= 1
        if word_lenght > 1:
            if letter == word:
              print('You won the game')

    #Replace 0 to 1 in the letter
        counter = 0
        position = 0
        reached = 0
        while counter != word_lenght:
            counter += 1
            while reached != 1:
                for i in alphabet:
                    if letter == i:
                        reached = 1
                        break
                    position += 1
        position_letter[position] = 1
if attemps == 0:
    print("there's no more attemps")

