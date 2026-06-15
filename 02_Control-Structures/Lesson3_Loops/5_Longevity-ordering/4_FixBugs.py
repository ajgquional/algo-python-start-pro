time = int(input('Enter the current time in hours: '))
while time >= 10 and time < 24:
    print("We're open")
    time = int(input('Enter the current time in hours: '))
print("We're closed. Hours of operation: 10 to 24.")
