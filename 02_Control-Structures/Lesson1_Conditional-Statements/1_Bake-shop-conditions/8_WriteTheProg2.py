wish = input('Wish: ')
wish = wish.lower()
suggest = wish == 'sugar free' or wish == 'fat free' or wish == 'gluten free'
print('Offer diet products:', suggest)