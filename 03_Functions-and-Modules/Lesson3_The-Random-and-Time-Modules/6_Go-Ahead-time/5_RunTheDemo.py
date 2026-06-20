from time import sleep

max_count = int(input('Enter the number of seconds: '))
counter = max_count
while counter > 0:
    print(counter)
    counter -= 1
    sleep(1)

