# Read in people profile from file (name, location, sstatus, employer, job) and print them out in table

# Sort the table and print it out

# Keep a dictionary of  people, key being their name, and create a loop to allow end user to input the name of a person, and  print out their profile

# sorted by location
# sorted by employer
from operator import itemgetter

people_list = []
people_dict = dict()

with open('people.csv', 'r') as people_file:
	for person_info in people_file:
		person_list = person_info.strip().split(',')

		person_info = dict()
		person_info['name'] = person_list[0]
		person_info['location'] = person_list[1]
		person_info['city'] = person_list[2]
		person_info['state'] = person_list[3]
		person_info['income'] = person_list[4]

		people_list.append(person_info)

	for person_info in people_list:
		if person_info['name'] not in people_dict:
			people_dict[person_info['name']] = person_info

		


print('--- UNSORTED PEOPLE -------------------------------------------')
print('')
print('{0:20}    {1:24}    {2:8}    {3:6}    {4:10}'.format('Name', 'Location', 'City', 'State', 'Income'))
print('{0:20}    {1:24}    {2:8}    {3:6}    {4:10}'.format('-'*20, '-'*24, '-'*8, '-'*6, '-'*10))

for person_info in people_list:
	print('{0:20}    {1:24}    {2:8}    {3:6}    {4:10}'.format(person_info['name'], person_info['location'], person_info['city'], person_info['state'], person_info['income']))


print('')
print('--- PEOPLE SORTED BY LOCATION -------------------------------------------')

print('')
print('{0:20}    {1:24}    {2:8}    {3:6}    {4:10}'.format('Name', 'Location', 'City', 'State', 'Income'))
print('{0:20}    {1:24}    {2:8}    {3:6}    {4:10}'.format('-'*20, '-'*24, '-'*8, '-'*6, '-'*10))
for person_info in sorted(people_list, key=itemgetter('location')):
	print('{0:20}    {1:24}    {2:8}    {3:6}    {4:10}'.format(person_info['name'], person_info['location'], person_info['city'], person_info['state'], person_info['income']))


print('')
print('--- PEOPLE SORTED BY NAME -------------------------------------------')

print('')
print('{0:20}    {1:24}    {2:8}    {3:6}    {4:10}'.format('Name', 'Location', 'City', 'State', 'Income'))
print('{0:20}    {1:24}    {2:8}    {3:6}    {4:10}'.format('-'*20, '-'*24, '-'*8, '-'*6, '-'*10))
for person_info in sorted(people_list, key=itemgetter('name')):
	print('{0:20}    {1:24}    {2:8}    {3:6}    {4:10}'.format(person_info['name'], person_info['location'], person_info['city'], person_info['state'], person_info['income']))



while True:
	name_to_find = input('\n\nEnter name to find: ')

	if len(name_to_find) == 0:
		break

	if name_to_find not in people_dict:
		print(f'I don\'t know anyone by the name of {name_to_find}')
		continue

	person_info = people_dict[name_to_find]
	print('')
	print('{0:20}    {1:24}    {2:8}    {3:6}    {4:10}'.format('Name', 'Location', 'City', 'State', 'Income'))
	print('{0:20}    {1:24}    {2:8}    {3:6}    {4:10}'.format('-'*20, '-'*24, '-'*8, '-'*6, '-'*10))
	print('{0:20}    {1:24}    {2:8}    {3:6}    {4:10}'.format(person_info['name'], person_info['location'], person_info['city'], person_info['state'], person_info['income']))