########################################
#                                      #
#     Day 12 - Number Guessing Game    #
#                                      #
########################################

import assets.day12_art as art
from random import randint


def get_input(msg, type):

    while True:

        inp = input(msg)

        try:
            assert len(inp) > 0, "Invalid input!"
            
            if type == 'difficulty':
                assert inp.lower()[0] in ('ehq'), "Invalid input! Enter 'easy', 'hard', or 'quit':"
            if type == 'guess':
                assert inp.isdigit() and int(inp) in range(1, 101), "Invalid guess! Guess a number between 1 and 100"
            if type == 'restart':
                assert inp.lower()[0] in ('yn'), "Invalid input! Enter 'yes' to restart or 'no' to quit:"

        except AssertionError as errMsg:
            print(errMsg)
            continue

        break

    return inp.lower()[0] if type in ('difficulty', 'restart') else int(inp)


def main():

    print(art.opening)
    print('Welcome to the Number Guessing Game!')

    new_game = True

    while True:

        if new_game:
            print("\nI'm thinking of a number between 1 and 100...\n")
            answer = randint(1, 100)
            game_over = False
            #print(f"Pssst, the answer is {answer}")

            difficulty = get_input("Choose a difficulty. Type 'easy' or 'hard': ", 'difficulty')
            
            if difficulty == 'e':
                full_chances = 10
                chances = 10
            elif difficulty == 'h':
                full_chances = 5
                chances = 5
            else:
                break

        print(f"\nYou have {chances} chances remaining...\n")

        guess = get_input("Make a guess: ", "guess")

        if guess > answer:
            print("Too high!")
            chances -= 1
        elif guess < answer:
            print("Too low!")
            chances -= 1
        else:
            tries = full_chances - chances + 1
            print(f"\nCorrect! I'm thinking of {guess}. You guessed it in {tries} tr{'y' if tries == 1 else 'ies'}!\n")
            game_over = True

        if chances == 0:
            print(f"\nYou're out of guesses... I was thinking of {answer}...\n")
            game_over = True

        if game_over:
            if get_input("Enter 'yes' to restart or 'no' to quit: ", 'restart') == 'y':
                new_game = True
            else:
                break
        else:
            new_game = False

    print('\nGoodbye!\n')


if __name__ == '__main__':

    main()