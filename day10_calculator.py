###############################
#                             #
#     Day 10 - Calculator     #
#                             #
###############################

import assets.day10_art as art
import math


def get_input(type):

    while True:

        inp = input()

        try:
            assert len(inp) > 0, "Invalid input!"
            
            if type == 'opr':
                assert inp in ("+", "-", "*", "/"), "Invalid input! Enter ' + ', ' - ', ' * ', or ' / ':"
            if type == 'num':
                assert inp.isdigit()  or (inp[0] == '-' and inp[1:].isdigit()), "Invalid input! Enter a valid number:"
            if type == 'restart':
                assert inp.lower()[0] in ('y', 'n') or inp.lower() == 'exit', "Invalid input! Enter 'Y' to continue calculation with result, 'N' to restart, or 'exit' to leave:"
        
        except AssertionError as msg:
            print(msg)
            continue

        return inp


def get_opr():

    print('''+
-
*
/
Pick an operation:''')

    return get_input('opr')[0]


def get_num(n):

    if n == 1:
        print("What's the first number?:")
    else:
        print("What's the next number?:")

    return float(get_input('num'))


def get_restart():

    choice = get_input('restart')

    if choice.lower()[0] == 'e':
        return 2
    elif choice.lower()[0] == 'n':
        return 1
    else:
        return 0


def calc_add(num1, num2):
    
    return num1 + num2


def calc_sub(num1, num2):
    
    return num1 - num2


def calc_multi(num1, num2):
    
    return num1 * num2


def calc_div(num1, num2):
    
    return num1 / num2


def calculate(opr, num1, num2):

    if opr == '+':
        return calc_add(num1, num2)
    
    if opr == '-':
        return calc_sub(num1, num2)

    if opr == '*':
        return calc_multi(num1, num2)

    if opr == '/':
        return calc_div(num1, num2)


def main():

    print(art.opening)

    result = math.inf

    while True:

        if result == math.inf:
            num1 = get_num(1)
            opr = get_opr()
            num2 = get_num(2)

        else:
            num1 = result
            opr = get_opr()
            num2 = get_num(2)

        output = calculate(opr, num1, num2)

        print()
        print(f'Result: {num1} {opr} {num2} = {output}')

        print()
        print(f"Type 'Y' to continue calculating with {output}, or type 'N' to start a new calculation:")
        print()
        restart = get_restart()

        if restart:
            if restart == 2:
                break
            else:
                print()
                result = math.inf

        else:
            print()
            print(f'First number: {output}')
            result = output


if __name__ == '__main__':

    main()
    print()
    print('Goodbye!')
    print()