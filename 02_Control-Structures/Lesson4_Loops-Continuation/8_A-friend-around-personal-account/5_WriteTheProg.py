number = input('Enter 1 - recommendation, 2 - draw, off - exit ')
while number != 'off':
   if number == '1':
       preference = input('Enter your preference: ')
       if preference == 'sports':
           print('Hardcore Sports Podcast')
       else:
           print("Kanye West's new album")
   elif number == '2':
       for i in range(1, 4):
           if input('Enter the name of the band: ') == 'Queen':
               print('You win a concert ticket!')
               break
   number = input('Enter 1 - recommendation, 2 - draw, off - exit ')
