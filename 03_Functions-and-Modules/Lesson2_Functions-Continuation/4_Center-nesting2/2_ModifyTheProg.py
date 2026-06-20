def calc_bmi(weight, height): # weight in kg, height in m
    index = weight / (height * height)
    return index


def print_recomendation(weight, height):
    index = calc_bmi(weight, height)
    if index <= 18.5:
        print('You are underweight, please go to room 301 for a consultation.')
    elif index > 18.5 and index <= 25:
        print('Your weight is normal, please go to the 3rd floor to continue the examination.')
    else:
        print('You are overweight, please go to room 410 for a consultation.')


weight = float(input('Enter weight (in kg): '))
height = float(input('Enter height (in m): '))
print_recomendation(weight, height)
