import random

r = random.randint(1,100)
while True:
	num = input('please input a number: ')
	num = int(num)
	if num == r:
		print('you got it!')
		break
	elif num > r:
		print('more then answer')
	else num < r:
		print('lower than anser')
		