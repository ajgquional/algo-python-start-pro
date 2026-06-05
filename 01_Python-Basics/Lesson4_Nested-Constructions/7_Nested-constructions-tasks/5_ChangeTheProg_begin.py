price_human = input('Airplane ticket price:')
price_luggage = input('Baggage transportation price:')
price_meal = input('Onboard meals price:')
price_human = int(price_human)
price_luggage = int(price_luggage)
price_meal = int(price_meal)
total = price_human + price_luggage + price_meal
print('To pay:', total)