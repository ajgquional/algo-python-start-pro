category = input('Enter the type of confectionery product: ')
price = int(input('Enter reasonable price: '))
category = category.lower()
is_sale = category == 'pastries' and price <= 500
print('Offer products for a promotion:', is_sale)