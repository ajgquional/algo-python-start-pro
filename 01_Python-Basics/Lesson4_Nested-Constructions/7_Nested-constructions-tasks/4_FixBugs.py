feedback = input('Leave a travel review: ')
feedback = feedback.lower()
print('Review length:', len(feedback))
print('Negativity search:', feedback.find('awful'))