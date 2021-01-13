from operator import itemgetter
from datetime import date 
import calendar 



def print_header(name, account_no, balance):
	print('name:', name, '    account:', account_no, '    balance:', '$' + str(balance))

def get_date(date_string):
	year = int(date_string[:4])
	month = int(date_string[4:6])
	day = int(date_string[6:8])

	return date(year, month, day)

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



def print_charges_from_list(charges_list, balance):
	print('Vendor                      Year   Month      Day      Charge      Balance')
	print('-------------------------   ----   --------   ----     --------    --------')
	for charge_info in charges_list:
		balance = balance - float(charge_info['charge'])
		charge_date = get_date(charge_info['date'])
		print('{:24}    {:4}   {:9}  {:4}    {:8,.2f}    {:8,.2f}'.format(charge_info['vendor'], 
			charge_date.year,
			calendar.month_name[charge_date.month],
			charge_date.day, 
			float(charge_info['charge']), 
			balance))


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


