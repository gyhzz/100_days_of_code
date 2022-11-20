#########################################################
#                                                       #
#     Day 3 - Treasure Island Interactive Text Game     #
#                                                       #
#########################################################

import assets.day3_art as art

opening = art.opening


def road_choice(choice):

    if choice == 'left':
        print('''You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.''')
        return lake_choice(get_input())
    else:
        return 'You fell into a hole. Game over.'


def lake_choice(choice):

    if choice == 'wait':
        print('''You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?''')
        return island_choice(get_input())
    else:
        return 'You get attacked by an angry trout. Game over.'


def island_choice(choice):
    
    if choice == 'yellow':
        return 'You found the treasure! You win!'
    elif choice == 'red':
        return "It's a room full of fire. Game over."
    elif choice == 'blue':
        return "You enter a room of beasts. Game over."
    else:
        return "You chose a door that doesn't exist. Game over."


def get_input():

    return input().lower()


def main():

    while True:

        print(opening)
        print('''Welcome to Treasure Island.
Your mission is to find the treasure.''')
        print('''You're at a cross road. Where do you want to go? Type "left" or "right"''')
        message = road_choice(get_input())
        break

    print(message)


if __name__ == '__main__':

    main()