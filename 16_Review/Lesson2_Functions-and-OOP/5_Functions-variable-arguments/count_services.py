# Bonus 1 - Create a Module

def count_services(**kwargs):
    total = 0
    categories = 0
    for category in kwargs:
        if kwargs[category] > 0:
            total += kwargs[category]
            categories += 1
    return total, categories
