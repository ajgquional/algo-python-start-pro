print('Adult ticket price (18-65) - 1500')
print('Child ticket price (under 18) - 1100')
print('Senior citizen ticket price (over 65) - 900')

adult_amount = int(input('Total adults: '))
children_amount = int(input('Total children: '))
retired_amount = int(input('Total senior citizens: '))
total = adult_amount*1500 + children_amount*1100 + retired_amount*900

print('To pay:', total)