################################
#                              #
#     Day 7 - Hangman Game     #
#                              #
################################

import assets.day7_art as art
import random


def word_gen():

    word_list = ['die', 'broadcast', 'native', 'dash',
     'Bible', 'add', 'brink', 'angel', 'colorful', 'convention',
      'role', 'perceive', 'retirement', 'bang', 'craftsman',
       'element', 'throne', 'preoccupation', 'matter', 'check']

    word = word_list[random.randint(0, len(word_list) - 1)]

    return word


def print_title():

    print(art.title)


def print_state(hang):

    print(art.states[hang])


def get_letter():

    while True:
        guess = input('Guess a letter: ')

        try:
            assert len(guess) == 1 and guess.isalpha() or guess.lower() == 'exit'

        except:
            print("Invalid input, only letters!")
            continue
    
        break

    return guess.lower()


def update_word(answer, current, letter):

    for i in range(len(answer)):
        if letter == answer[i]:
            current = current[:i] + letter + current[i + 1:]

    return current


def main():

    answer = word_gen()
    current_word = ''.join(['_' for _ in answer])
    correct_guesses = []
    hang = 0
    game_over = False
    print(answer)

    while not game_over:

        guess = get_letter()

        if guess == 'exit':
            break

        if guess in answer:
            if guess in correct_guesses:
                print(f'You already guessed {guess}!')
            else:
                current_word = update_word(answer, current_word, guess)
                if current_word == answer:
                    print('You win!')
                    game_over = True
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            hang += 1

        if hang == len(art.states) - 1:
            print('Game over!')
            game_over = True

        print(' '.join([char for char in update_word(answer, current_word, guess)]))
        print_state(hang)
        print()


if __name__ == '__main__':

    print()
    print_title()
    print()
    main()
    print()
    print('Goodbye!')
    print()