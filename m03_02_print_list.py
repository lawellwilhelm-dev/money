balance = 1000
name = 'Lawell Wilhelm'
account_no = '01123581321'


print('name:', name, '    account:', account_no, '    balance:', '$' + str(balance))


charges_file = open('m00_charges-file')
for charge_info_string in charges_file:
	charge_info = charge_info_string.strip().split(',')
	print(charge_info)