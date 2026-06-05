while True:
    try:
        children_amount = int(input('Enter the number of children'))
        sweets_amount = int(input('Enter the number of candies'))
        break
    except:
        print('Error! The number must be an integer')
#add portion calculation with processing of division by 0