from operator import itemgetter

balance = 1000
name = 'Lawell Wilhelm'
account_no = '01123581321'


print('name:', name, '    account:', account_no, '    balance:', '$' + str(balance))

charges_list = []
for charge_info in open('m00_charges-file'):
	charge_info_list = charge_info.strip().split(',')

	charge_info = dict()
	charge_info['vendor'] =charge_info_list[0]
	charge_info['date'] =charge_info_list[1]
	charge_info['charge'] =charge_info_list[2]
	
	charges_list.append(charge_info)

print('\n')
print('Vendor                      Date          Charge      Balance')
print('-------------------------   --------      --------    --------')
for charge_info in charges_list:
	balance = balance - float(charge_info['charge'])
	print('{0:24}    {1:10}    {2:8,.2f}    {3:8,.2f}'.format(charge_info['vendor'], charge_info['date'], float(charge_info['charge']), balance))


balance = 1000
charges_sorted_by_date = sorted(charges_list, key=itemgetter('date'))

print('\n')
print('Vendor                      Date          Charge      Balance')
print('-------------------------   --------      --------    --------')
for charge_info in charges_sorted_by_date:
	balance = balance - float(charge_info['charge'])
	print('{0:24}    {1:10}    {2:8,.2f}    {3:8,.2f}'.format(charge_info['vendor'], charge_info['date'], float(charge_info['charge']), balance))