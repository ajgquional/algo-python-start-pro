def amount_five():
    grade = int(input('Grade (0 - stop): '))
    amount_five = 0
    while grade != 0:
        if grade == 5:
            amount_five += 1
        grade = int(input('Grade (0 - stop): '))
    return amount_five


def set_discount():
    amount = amount_five()
    if amount >= 4 and amount <= 5:
        return 10
    elif amount > 5:
        return 15
    else:
        return 0


print('Discount on theater tickets (%):', set_discount())
