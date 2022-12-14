######################################
#                                    #
#     Day 7 - Hangman Game (Art)     #
#                                    #
######################################

title = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/'''

states = ['''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']