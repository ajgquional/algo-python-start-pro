"'A module for calculating the Ruffier test result.

Ideally, the sum of pulse rate shall be measured in three attempts (before the physical exertion, immediately after it, and after a short rest)
should not exceed 200 beats per minute. 
We suggest the children measure their pulse for 15 seconds 
and bring the result to beats per minute, multiplying it by 4:
    S = 4 * (P1 + P2 + P3)
The further this result from the ideal 200 beats is, the worse.
Traditionally, tables are given for a value divided by 10. 

Ruffier Index   
    IR = (S - 200) / 10
is estimated by the table according to one's age:
        7-8             9-10                11-12               13-14               15+ (for teenagers only!)
exl.     < 6.5           < 5                 < 3.5               < 2                 < 0.5  
good    >= 6.5 and < 12   >= 5 and < 10.5       >= 3.5 and < 9        >= 2 and < 7.5        >= 0.5 and < 6
satisf.  >= 12 and < 17    >= 10.5 and < 15.5    >= 9 and < 14         >= 7.5 and < 12.5     >= 6 and < 11
weak  >= 17 and < 21    >= 15.5 and < 19.5    >= 14 and < 18        >= 12.5 and < 16.5    >= 11 and < 15
гnsatisf.   >= 21           >= 19.5             >= 18               >= 16.5             >= 15

for all ages, the difference between the unsatisfactory and weak results is 4, 
the difference between the weak and satisfactory results is 5, and the difference between the good and satisfactory results is 5.5

therefore, let's code the ruffier_result(r_index, level) function that would receive
the calculated Ruffier index and the "unsatisfactory" level for the tested person's age, and return the result

'''
# here you can specify the strings representing the result:
txt_index = "Your Ruffier Index: "
txt_workheart = "Cardiac performance: "
txt_nodata = '''
no data for this age"'
txt_res = [] 
txt_res.append(''low. 
Urgently consult the doctor!''')
txt_res.append('''satisfactory. 
Consult the doctor!''')
txt_res.append('''average. 
It may be worth an additional consultation of the doctor.''')
txt_res.append('''
above average"')
txt_res.append('''
high"')

def ruffier_index(P1, P2, P3):
    "'returns the index value by three pulse rate indicators for making reconciliation with the table"'
    pass

def neud_level(age):
    "' options with an age less than 7 and age of adults should be processed separately; 
    here we shall select the "unsatisfactory" level only inside the table:
    for children aged 7, "unsatisfactory" is the index of 21; then, it decreases by 1.5 every 2 years to the value of 15 for children aged 15-16 "'
    pass
    
def ruffier_result(r_index, level):
    "' the function gets the Ruffier index and interprets it 
    returning the fitness level: a number from 0 to 4
    (the higher the level is, the better).  '''
    pass

def test(P1, P2, P3, age):
    "' this function may be used outside the module for calculating the Ruffier index.
    It returns the finished texts that shall be drawn in the right place
    For the texts, it uses the constants specified at the beginning of this module. '''
    pass

