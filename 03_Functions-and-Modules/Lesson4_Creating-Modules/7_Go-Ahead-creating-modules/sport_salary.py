# Task 6

def get_full_time(experience):
    #coach's salary with multiplying factor
    salary = 20000
    if experience >= 3 and experience < 5:
        k = 1.5
    elif experience >= 5 and experience < 7:
        k = 2
    elif experience >= 7:
        k = 3
    else:
        k = 1
    salary *= k
    return salary


def get_part_time(hours):
    #coach's salary with hourly pay
    per_hour = 800
    salary = hours*per_hour
    return salary

