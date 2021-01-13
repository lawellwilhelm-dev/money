balance = 1000.0
name = 'Nelson Olumide'
account_no = '01123581231'

print('Name:', name, '    account:', account_no, '    original balance:', '$' + str(balance))

charges = [5.99, 12.45, 28.05]

for charge in charges:
	balance = balance - charge
	print('Name:', name, '    account:', account_no, '    charge:', charge, '    new balance    ', '$' + str(balance))

