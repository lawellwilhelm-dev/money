print('\n')
print('---- People ----------------------------------------')

number_people = 0
with open('people', 'r') as people_file:

	for person in people_file:
		number_people += 1
		print(number_people, '    name:', person.strip())


print('\n')
print('Total people:', number_people)
