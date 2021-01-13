from operator import itemgetter
from m05_03_functions_module_util import print_header
from m05_03_functions_module_util import read_charges
from m05_03_functions_module_util import print_charges_from_list
from m05_03_functions_module_util import print_charges_from_dict

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