def calc_bmi(weight, height): #weight in kg, height in m    
    index = weight / (height * height)
    return index
 
#def print_recomendation(weight, height):
 
weight = float(input('Enter weight (kg):'))
height = float(input('Enter height (m):'))
print_recomendation(weight, height)
