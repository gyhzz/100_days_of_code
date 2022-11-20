#################################
#                               #
#     Day 9 - Blind Auction     #
#                               #
#################################

import assets.day9_art as art
import os


def get_input(type):

    while True:
        inp = input()

        try:
            assert len(inp) > 0, "Enter your name:" if type == 'name' else ""

            if type == 'add':
                assert inp.lower()[0] in ('y', 'n'), "Enter 'yes' or 'no':"
            elif type == 'bet':
                assert inp.isdigit(), "Enter a positive price ($):"
        
        except AssertionError as msg:

            print(f"Invalid input! {msg}")
            continue

        return inp


def add_players():

    print("Are there any other bidders? Type 'yes or 'no':")

    if get_input('add').lower()[0] == 'y':
        return 1
    else:
        return 0


def player_name():

    print('What is your name?:')
    return get_input('name')


def player_bet():

    print('What is your bid?:')
    return int(get_input('bet'))


def main():

    print(art.opening)
    bets = {}
    highest_bidders = []

    while True:
        player = player_name()
        bet = player_bet()
        bets[player] = bet

        os.system('cls')

        if not add_players():
            break

    highest = max(bets.values())

    for k, v in bets.items():
        
        if v == highest:
            highest_bidders.append(k)

    msg = f" is {highest_bidders[0]} with the highest bid of"
    msg = f"s are {', '.join([p for p in highest_bidders])} with highest bids of" if len(highest_bidders) > 1 else msg

    print(f'The winner{msg} {highest}!')


if __name__ == '__main__':

    main()
    print()