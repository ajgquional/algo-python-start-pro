class Price_list():
   def __init__ (self,name):
       self.name = name
       self.pricelist = dict()
   def add_price(self, **kwargs):
       for key in kwargs:
           self.pricelist[key] = kwargs[key]
   def order(self, **kwargs):
       sum = 0
       for key in kwargs:
           if key in self.pricelist:
               sum += self.pricelist[key] * kwargs[key]
       return sum
 
my_offer = Price_list('Instagram')
my_offer.add_price(management = 1000, content_plan = 850, style = 500, stories = 100, post = 300)
while input('Would you like to make an order? (1 - yes, 0 - no): ') != '0':
    operation = input('Would you like to order management of your accounts (1) or posts (2)?: ')
    if operation == '1':
        management = int(input('How many new accounts would you like to add?: '))
        content_plan = int(input('For how many of those will we create a content plan?: '))
        style = int(input('For how many of those will we develop a style?: '))
        price = my_offer.order(management = management, content_plan = content_plan, style = style)
    else:
        stories = int(input('How many stories would you like to order?: '))
        post = int(input('How many posts would you like to order?: '))
        price = my_offer.order(stories = stories, post = post)
    print(f'Service cost: {price} coins.')
 
print('Thank you for working with us! Have a nice day!')
