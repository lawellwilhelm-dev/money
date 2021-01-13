from operator import itemgetter


def print_header(name, account_no, balance):
	print('name:', name, '    account:', account_no, '    balance:', '$' + str(balance))

def read_charges(charges_file):
	charges_list = []
	charges_dict = dict()
	for charge_info in open(charges_file):
		charge_info_list = charge_info.strip().split(',')

		charge_info = dict()
		charge_info['vendor'] = charge_info_list[0]
		charge_info['date'] = charge_info_list[1]
		charge_info['charge'] = charge_info_list[2]
		
		charges_list.append(charge_info)

		if charge_info['vendor'] not in charges_dict:
			charges_dict[charge_info['vendor']] = list()

		charges_dict[charge_info['vendor']].append(charge_info)

	return charges_list, charges_dict


def print_charges_from_dict(charges_dict, balance):
	print('Vendor                      Date          Charge      Balance')
	print('-------------------------   --------      --------    --------')
	for vendor, charge_info_list in charges_dict.items():
		for charge_info in charge_info_list:
			balance = balance - float(charge_info['charge'])
			print('{0:24}    {1:10}    {2:8,.2f}    {3:8,.2f}'.format(charge_info['vendor'], charge_info['date'], float(charge_info['charge']), balance))

	

def print_charges_from_list(charges_list, balance):
	print('Vendor                      Date          Charge      Balance')
	print('-------------------------   --------      --------    --------')
	for charge_info in charges_list:
		balance = balance - float(charge_info['charge'])
		print('{0:24}    {1:10}    {2:8,.2f}    {3:8,.2f}'.format(charge_info['vendor'], charge_info['date'], float(charge_info['charge']), balance))


#-------------------------------------------------------------------------

# Initialize and print account information
balance = 1000.00
name = 'Kweku Kweku'
account_no = '01123581321'

print_header(name, account_no, balance)

# Read, sort, and print charges
charges_list, charges_dict = read_charges('m00_charges-file')
charges_sorted_by_date = sorted(charges_list, key=itemgetter('date'))


balance = 1000.00
print('\nUnsorted charges:')
print_charges_from_list(charges_list, balance)

balance = 1000.00
print('\nCharges sorted by date:')
print_charges_from_list(charges_sorted_by_date, balance)

balance = 1000.00
print('\nCharges from dictionary (random order):')
print_charges_from_dict(charges_dict, balance)

