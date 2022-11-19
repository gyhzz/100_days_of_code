##################################
#                                #
#     Day 2 - Tip Calculator     #
#                                #
##################################


if __name__ == '__main__':

	print('Welcome to the tip calculator!')

	bill = input('What was the total bill? $')

	tip = input('How much tip would you like to give? 10, 12, or 15? ')

	people = input('How many peopel to split the bill? ')

	total_bill = int(bill) * int(tip)

	per_person = total_bill/int(people)

	print(f'Each person should pay: ${per_person}')
