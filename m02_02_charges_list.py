balance = 1000.0
name = 'Nelson Olumide'
account_no = '01123581231'

print('Name:', name, '    account:', account_no, '    original balance:', '$' + str(balance))

charges = [5.99, 12.45, 28.05]

balance = balance - charges[0]
print('Name:', name, '    account:', account_no, '    charge:', charges[1], '    new balance    ', '$' + str(balance))
balance = balance - charges[1]
print('Name:', name, '    account:', account_no, '    charge:', charges[1], '    new balance    ', '$' + str(balance))
balance = balance - charges[2]
print('Name:', name, '    account:', account_no, '    charge:', charges[2], '    new balance    ', '$' + str(balance))
