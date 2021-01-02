# else if 
age = input('Please input age: ')
age = int(age)
if age < 13:
	print('elementary')
elif age >= 13 and age < 18:
	print('junior high school or high school')
elif age >= 18 and age < 22:
	print('College')
else:
	print('Member of society')