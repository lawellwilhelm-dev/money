balance = 1000.0
name = 'Nelson Olumide'
account_no = '01123581231'

print('Name:', name, '    account:', account_no, '    original balance:', '$' + str(balance))



charges_file = open('m00_charges-only-file')
for charge in charges_file:
	balance = balance - float(charge)
	print('Name:', name, '    account:', account_no, '    charge:', charge, '    new balance:   ', '$' + str(balance))
