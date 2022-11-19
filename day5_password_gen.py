######################################
#                                    #
#     Day 5 - Password Generator     #
#                                    #
######################################

import random

alpha = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
nums = '0123456789'
symbs = '''`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?'''


def get_input():

    while True:

        choice = input()

        try:
            assert choice.isdigit()
        except:
            print("Invalid input. Enter a valid number:")
            continue

        return int(choice)


def letters():

    print('How many letters would you like in your password?')
    choiceL = get_input()
    l_string = ''

    for _ in range(choiceL):
        l_string += alpha[random.randint(0, len(alpha) - 1)]

    return l_string


def symbols():

    print('How many symbols would you like in your password?')
    choiceS = get_input()
    s_string = ''

    for _ in range(choiceS):
        s_string += symbs[random.randint(0, len(symbs) - 1)]

    return s_string


def numbers():

    print('How many numbers would you like?')
    choiceN = get_input()
    n_string = ''

    for _ in range(choiceN):
        n_string += nums[random.randint(0, len(nums) - 1)]

    return n_string


def mixer(l, s, n):

    full_string = l + s + n
    full_list = [char for char in full_string]
    password = ''

    while len(full_list):
        password += full_list.pop(random.randint(0, len(full_list) - 1))

    return password


def main():

    print('Welcome to the PyPassword Generator!')
    
    password = mixer(letters(), symbols(), numbers())
    print(f'Your password is {password}')


if __name__ == '__main__':

    print()
    main()
    print()