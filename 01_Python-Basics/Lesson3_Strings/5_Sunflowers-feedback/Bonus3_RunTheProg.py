from time import *

start_time = time()
phrase = input('Write a review about us: ')
end_time = time()

total_time = end_time - start_time
symbols = len(phrase)
print('Print speed:', symbols/total_time*60)