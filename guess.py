import random

r = random.randint(1,100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('please input a number: ')
	num = int(num)
	if num == r:
		print('you got it!')
		print('This is ', count ,' times you guessed')
		break
	elif num > r:
		print('more then answer')
	else num < r:
		print('lower than anser')
	print('This is ', count ,' times you guessed')
