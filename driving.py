country = input('What is your citizenship? ')
age = input('What is your age? ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can take the driving test.')
	else:
		print('You cannot drive.')
elif country == 'USA':
	if age >= 16:
		print('You can take the driving test.')
	else:
		print('You cannot drive.')
else:
	print('The database is restricted to Taiwan and USA')
