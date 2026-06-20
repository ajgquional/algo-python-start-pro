from time import time

stopwatch = input('1 - start, 0 - stop: ')
while stopwatch != '0':
    if stopwatch == '1':
        start = time()
    else:
        print('Action not found!')
    stopwatch = input('0 - stop: ')
    
end = time()
total = int(end-start)
print('Total time:', total, 'sec')
