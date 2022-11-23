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

    return True if calc_hand(hand1) > calc_hand(hand2) else False


def is_draw(hand1, hand2):

    return True if calc_hand(hand1) == calc_hand(hand2) else False


def bust(hand):

    return 1 if calc_hand(hand) > 21 else 0


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
    bot_turn = True
    player_win = False
    bot_win = False
    player_bust = False
    bot_bust = False

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

        new_game = False

        if player_turn:

            print("Would you like to draw 'Y' or hold 'N':")
            if get_input() == 'y':
                player.append(cards[random.randint(0, len(cards) - 1)])
            else:
                player_turn = False

            show_deck(player)
            print(f"AI hand: [ {bot[0]} {'#' * (len(bot) - 1)} ]")

            if bust(player):
                print('You went bust!')
                player_bust = True
                player_turn = False

            elif len(player) == 5:
                print('You win!')
                player_win = True
                player_turn = False
        
        else:

            if calc_hand(bot) < 17:
                bot.append(cards[random.randint(0, len(cards) - 1)])
            else:
                bot_turn = False

            show_deck(player)
            print(f"AI hand: [ {bot[0]} {'#' * (len(bot) - 1)} ]")

            if bust(bot):
                print('AI went bust!')
                player_bust = True
                player_turn = False

            elif len(bot) == 5:
                print('AI win!')
                bot_win = True
                bot_turn = False

        if not player_turn and not bot_turn:

            if hand1_win(player, bot) and not player_bust:

                print('You win!')

            elif is_draw(player, bot):

                print("It's a draw!")
            
            elif hand1_win(bot, player):

                print('AI win!')

            print("Would you like to play again? Enter 'Y' or 'N':")
            if get_input() == 'n':
                break
            else:
                new_game = True


if __name__ == '__main__':

    main()