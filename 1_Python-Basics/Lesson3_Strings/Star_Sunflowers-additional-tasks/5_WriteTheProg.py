searching1 = 'fun'
searching2 = 'exciting'
searching3 = 'entertainment'
feedback = input('Rate the entertainment complex: ')
feedback = feedback.lower()
result1 = feedback.find('fun')
result2 = feedback.find('exciting')
result3 = feedback.find('entertainment')
print('Analysis results:', result1, result2, result3)