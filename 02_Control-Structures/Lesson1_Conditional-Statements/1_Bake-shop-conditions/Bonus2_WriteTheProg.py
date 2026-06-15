product = input('Product type: ')
taste = input('Filling: ')
product = product.lower()
taste = taste.lower()
suggest = product == 'cookie' and taste == 'cream' or product == 'cookie' and taste == 'jam'
print('Ordered a popular cookie with a filling:', suggest)