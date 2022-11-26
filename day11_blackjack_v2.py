###############################
#                             #
#     Day 11 - Blackjack 2    #
#                             #
###############################

import assets.day11_art as art
import time
from random import randint

cards = 'A23456789XJQK'


def get_input(inp_txt):

    while True:

        inp = input(inp_txt)

        try:
            assert len(inp) > 0, "Invalid input!"
            assert inp.lower()[0] in ('yne'), "Invalid input!"

        except AssertionError as errMsg:
            print(errMsg)
            continue

        break

    return inp.lower()[0]


def calc_hand(hand):

    card_values = [i if i <= 10 else 10 for i in range(1, len(cards) + 1)]
    total = 0

    for card in hand:
        total += card_values[cards.index(card)]

    if len(hand) == 2 and 'A' in hand:
        total += 10

    return total


def main():

    start_game = True
    
    while start_game:

        print(art.opening)

        if get_input("Enter 'Y' to start Blackjack or 'N' to exit: ") != 'y':
            break

        player = []
        player.append(cards[randint(0, len(cards) - 1)])
        player.append(cards[randint(0, len(cards) - 1)])

        dealer = []
        dealer.append(cards[randint(0, len(cards) - 1)])
        dealer.append(cards[randint(0, len(cards) - 1)])

        player_turn = True
        dealer_turn = True
        first_turn = True
        five_card_win = False
        player_bust = False
        dealer_bust = False

        print("\nYour turn...\n")
        while player_turn:

            print(f"Player's hand: {player}")
            print(f"Dealer's hand: {[dealer[i] if i == 0 else '.' for i in range(len(dealer))]}")

            if calc_hand(player) != 21 and get_input("\nType 'Y' to draw a card, 'N' to hold: ") == 'y':
                print()
                player.append(cards[randint(0, len(cards) - 1)])

                if calc_hand(player) > 21:
                    print('You went bust!')
                    player_turn = False
                    player_bust = True

                elif len(player) >= 5:
                    print(f"Player's hand: {player}")
                    print(f"Dealer's hand: {[dealer[i] if i == 0 else '.' for i in range(len(dealer))]}")
                    print('\nWow, 5 cards! You win!')
                    five_card_win = True
                    player_turn = False
                    dealer_turn = False

            else:

                if calc_hand(player) == 21:
                    print("You got Blackjack!")
                else:
                    print("You hold...\n")

                player_turn = False

        while dealer_turn:

            if first_turn:
                print("\nDealer's turn...\n")

            print(f"Player's hand: {player}")
            print(f"Dealer's hand: {[dealer[i] if i == 0 else '.' for i in range(len(dealer))]}")

            print('\nThinking...\n')
            time.sleep(3)
            
            if calc_hand(dealer) < 17:
                dealer.append(cards[randint(0, len(cards) - 1)])

                if calc_hand(dealer) > 21:
                    print('Dealer went bust!')
                    dealer_turn = False
                    dealer_bust = True

            elif calc_hand(dealer) == 21:
                print("Dealer has Blackjack!")
                dealer_turn = False

            else:
                print("Dealer holds...\n")
                dealer_turn = False
            
            first_turn = False

        if not five_card_win:

            player_score = calc_hand(player)
            dealer_score = calc_hand(dealer)

            print(f"Player's hand: {player}")
            print(f"Dealer's hand: {dealer}")

            print(f"\nPlayer points: {player_score}, Dealer points: {dealer_score}\n")

            player_win = not player_bust and (player_score > dealer_score or dealer_bust)
            dealer_win = not dealer_bust and (dealer_score > player_score or player_bust)

            if player_win and dealer_win:
                print("It's a draw!")
            elif player_win:
                print("Player wins!")
            elif player_score == dealer_score or (player_bust and dealer_bust):
                print("It's a draw!")
            else:
                print("Dealer wins!")

        if get_input("\nGame ended. Enter 'Y' to restart or 'n' to exit: ") != 'y':
            start_game = False

    print("\nGoodbye!\n")


def tester(p, d):

    player_bust = True if p > 21 else False
    dealer_bust = True if d > 21 else False

    player_score = p
    dealer_score = d

    print(f"Player's hand: {p}")
    print(f"Dealer's hand: {d}")

    player_win = not player_bust and (player_score > dealer_score or dealer_bust)
    dealer_win = not dealer_bust and (dealer_score > player_score or player_bust)

    if player_win and dealer_win:
        return 'Draw'
    elif player_win:
        return 'Player'
    elif player_score == dealer_score or (player_bust and dealer_bust):
        return 'Draw'
    else:
        return 'Dealer'


def test():

    scenarios = ((21,20,'Player'),(20,21,'Dealer'),(21,21,'Draw'),(25,20,'Dealer'),(20,25,'Player'),(15,13,'Player'),(25,25,"Draw"),(10,12,'Dealer'),(10,21,'Dealer'),(21,10,'Player'))

    for scenario in scenarios:

        correct = scenario[2]
        program = tester(scenario[0], scenario[1])

        print(f'Correct: {correct}')
        print(f'Program: {program}')
        if correct != program:
            print('Wrong')
        else:
            print('Correct')

        print()


if __name__ == '__main__':

    main()