max_price = int(input('How much are you willing to spend on dessert? '))
if max_price < 500:
    print('Try the dulce de leche cakes!')
if max_price >= 500 and max_price <= 1000:
    print('Treat yourself to the Secret cake!')
if max_price > 1000:
    print('Treat yourself to the chocolate lava cake with blueberries!')