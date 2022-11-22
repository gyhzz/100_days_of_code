##############################
#                            #
#     Day 11 - Blackjack     #
#                            #
##############################

import assets.day11_art as art
import random

cards = 'A23456789XJQK'


def get_input():

    while True:

        inp = input()

        try:
            assert len(inp) > 0 and inp.lower()[0] in 'yne', "Invalid input!"
        except AssertionError as msg:
            print(msg)
            continue

        break

    return inp.lower()[0]


def calc_hand(hand):

    total = 0

    for card in hand:
        value = cards.index(card) + 1
        
        if value <= 10 and len(hand) != 2:
            total += value
        else:
            spc_add = 10 if card in 'XJQK' else value

            if card == 'A':
                spc_add = 11 if card == 'A' and hand.count('A') != 2 else 1

            total += spc_add

    return total


def hand1_win(hand1, hand2):

    if hand1 > hand2:
        return True
    else:
        return False


def bust(hand):

    return 1 if hand > 21 else 0


def show_deck(hand):

    print('Your hand: [ ', end='')
    for i in range(len(hand)):
        print(f"{hand[i]}", end=' ')

    print(']')


def turn_draw(hand):

    hand.append(cards[random.randint(0, len(cards) - 1)])


def main():

    print(art.opening)

    player = []
    bot = []
    new_game = True
    player_turn = True

    while True:

        if new_game:
            player = []
            bot = []
            player.append(cards[random.randint(0, len(cards) - 1)])
            player.append(cards[random.randint(0, len(cards) - 1)])
            bot.append(cards[random.randint(0, len(cards) - 1)])
            bot.append(cards[random.randint(0, len(cards) - 1)])
        
        show_deck(player)
        print(f"AI hand: [ {bot[0]} {'#' * (len(bot) - 1)} ]")

        turn_draw(player)
        turn_draw(player)
        turn_draw(player)

        show_deck(player)

        break


if __name__ == '__main__':

    main()