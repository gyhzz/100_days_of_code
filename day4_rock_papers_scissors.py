#########################################
#                                       #
#     Day 4 - Rock, Paper, Scissors     #
#                                       #
#########################################
import random


wins = {0: 2, 1: 0, 2: 1}


def display_option(choice):

    if choice == 0:
        print('''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')

    elif choice == 1:
        print('''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')

    elif choice == 2:
        print('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')


def get_choice():

    choice = input()

    if choice.lower() != 'exit':

        try:
            assert choice in ('012')
        except:
            choice = random.randint(0, 2)
    
    else:
        return 'exit'

    return int(choice)


def player_won(player, ai):

    if player == ai:
        return 2

    for k, v in wins.items():
        if player == k and ai == v:
            return 1

    return 0


def main():

    while True:

        print('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:')

        player_choice = get_choice()
        if player_choice == 'exit':
            break

        print()
        print('You choose:')
        display_option(player_choice)

        ai_choice = random.randint(0, 2)

        print()
        print('Computer chooses:')
        display_option(ai_choice)

        # print(f'Player: {player_choice}')
        # print(f'AI Choice: {ai_choice}')

        result = player_won(player_choice, ai_choice)

        print()
        if result:
            if result == 2:
                print("It's a draw.")
            else:
                print("You win!")
        else:
            print("You lose.")

        print()

    print()
    print('Goodbye!')
    print()


if __name__ == '__main__':

    print()
    main()