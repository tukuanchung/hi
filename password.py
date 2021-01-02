i = 0
while  i < 3:
	password = input('Please input password: ')
	if password == 'a123456':
		print('Login successs!')
		break;
	else:
		i = i + 1

		if i == 3:
			break
		print('Wrong Password!')
		print('You have ', (3-i), ' oppoturnites')