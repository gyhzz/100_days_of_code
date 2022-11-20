#################################
#                               #
#     Day 8 - Caesar Cipher     #
#                               #
#################################

import assets.day8_art as art

all_chars = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?'''


def check_input(type):

    while True:

        inp = input()

        try:
            if type == 'choice':
                assert inp.lower()[0] in ('e', 'd'), "Invalid input! Enter 'encode' or 'decode':"
            elif type == 'message':
                assert len(inp) > 0, "Message cannot be empty!"
            elif type == 'count':
                assert inp.isdigit(), "Enter a valid number!"
            elif type == 'continue':
                assert inp.lower()[0] in ('y', 'n'), "Invalid input! Enter 'Yes' or 'No':"

        except AssertionError as msg:
            print(msg)
            continue

        return inp


def get_choice():

    print('''Type 'encode' to encrypt, type 'decode' to decrypt:''')
    return check_input('choice').lower()[0]


def get_message():

    print('Type your message:')
    return check_input('message')


def get_count():

    print('Type the shift number:')
    return int(check_input('count'))


def usr_continue():

    return check_input('continue').lower()[0]


def shuffle(action, message, count):

    result = ''

    if action == 'e':
        for char in message:
            pos = all_chars.index(char)
            new_pos = (pos + count) % len(all_chars)
            result += all_chars[new_pos]
        
    else:
        for char in message:
            pos = all_chars.index(char)
            new_pos = (pos - count) % len(all_chars)
            result += all_chars[new_pos]

    return result


def main():

    print(art.title)

    while True:

        choice = get_choice()
        output = shuffle(choice, get_message(), get_count())

        option = 'encode'
        option = 'decode' if choice == 'd' else option
        print(f'Your {option}d message: {output}')

        print("Type 'yes' if you want to go again. Otherwise type 'no':")
        if usr_continue() == 'y':
            continue
        else:
            break


if __name__ == '__main__':

    main()
    print()
    print('Goodbye!')
    print()