balance = 1000
name = 'Lawell Wilhelm'
account_no = '01123581321'


print('name:', name, '    account:', account_no, '    balance:', '$' + str(balance))

print('\nName                Account          Chage       Balance')
for charge in open('m00_charges-only-file'):
	balance = balance - float(charge)
	print('{0:16}    {1:10}    {2:8,.2f}    {3:8,.2f}'.format(name, account_no, float(charge), balance))