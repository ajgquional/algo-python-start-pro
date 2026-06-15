amount = int(input('How many videos have been published this month?: '))
total = 0
views_payment = 2.2
for i in range(amount):
    views = int(input('The number of views for video #' + str(i+1) + ': '))
    total += views//1000 * views_payment
    advt = input('Did the video have native advertising (yes/no)?: ').lower()
    if advt == 'yes':
        advt_payment = int(input('Enter the price of the integration: '))
        total += advt_payment
total = int(total)
print('Total earnings for the month:', total, 'USD.')
