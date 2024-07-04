# Hangman Game

This is a simple implementation of the classic Hangman game in Python. The player has to guess the hidden word by suggesting letters within a certain number of attempts.

## How to Play

1. The game will choose a random word from a predefined list.
2. A percentage of the letters in the word will be hidden.
3. The player will have a limited number of attempts to guess the letters or the entire word.
4. If the player guesses a correct letter, it will be revealed in the word.
5. If the player guesses the word correctly or reveals all letters before running out of attempts, they win.
6. If the player runs out of attempts, they lose.

## Prerequisites

- Python 3.x

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/CeciliaRava1/hangman-game.git
    cd hangman-game
    ```
2. Run the game:
    ```bash
    python hangman.py
    ```

## Code Explanation

The code consists of the following main parts:

1. **Variable Initialization:**
    ```python
    import secrets
    import random
    import math
    
    word_letters = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    position_letter = [0] * len(alphabet)
    list = ['cat', 'dog', 'rabbit', 'wolf', 'horse', 'cow', 'elephant', 'bird', 'fox']
    word = secrets.choice(list)
    word_game = ''
    word_length = len(word)
    position_word = []
    reached = 0
    position = 0
    counter = 0
    attempts = 3
    jupiter = []
    ```

2. **Discovering Letters of the Word Without Repetition:**
    ```python
    times = 0
    number = 0
    character = word[0]
    word_letters.append(word[0])
    for i in range(len(word) - 1):
        number += 1
        if character != word[number]:
            word_letters.append(word[number])
    ```

3. **Creating a Vector with Letters of the Word:**
    ```python
    for i in word:
        jupiter.append(i)
    ```

4. **Determining Position Numbers of Letters in the Alphabet:**
    ```python
    for i in word:
        reached = 0
        position = 0
        while reached != 1:
            if alphabet[position] == i:
                reached = 1
                position_word.append(position)
            else:
                position += 1
    ```

5. **Hiding a Percentage of Letters:**
    ```python
    hidden = 0
    coso = ''
    position = 0
    print(word)
    hide_percent = math.floor(word_length * 0.6)
    while hidden < hide_percent:
        for i in range(len(word)):
            random_number = random.randint(0, 1)
            if random_number == 1:
                hidden += 1
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
    ```

6. **Handling User Input and Game Logic:**
    ```python
    while attempts > 0:
        palabra = ''
        for i in range(len(position_word)):
            if position_letter[position_word[i]] == 1:
                palabra += alphabet[position_word[i]] + ' '
            else:
                palabra += '_ '
                
        if '_' not in palabra:
            print('You won')
            break
        else:
            letter = input(f'Write a letter or a word for {palabra}. Attempts: {attempts}')
            attempts -= 1
            if word_length > 1 and letter == word:
                print('You won the game')
                break

        counter = 0
        position = 0
        reached = 0
        while counter != word_length:
            counter += 1
            while reached != 1:
                for i in alphabet:
                    if letter == i:
                        reached = 1
                        break
                    position += 1
        position_letter[position] = 1

    if attempts == 0:
        print("There's no more attempts")
    ```

## Acknowledgments

Inspired by the classic Hangman game.

---

Feel free to contribute to this project by forking the repository and submitting pull requests. Happy coding!
