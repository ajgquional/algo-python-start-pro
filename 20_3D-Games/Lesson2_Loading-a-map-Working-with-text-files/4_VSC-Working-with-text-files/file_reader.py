# For the following tasks, uncomment groups of code to see the output for that task.
# The task is described below the task numbers.

# fix if the text file cannot be found even if it is in the same folder as the script
# this happens when the terminal does not point specifically to the folder where the script is located, but to a parent folder
from pathlib import Path
text_file = Path(__file__).with_name('my_file.txt')
# if the terminal directly points to the folder where the script is located, simply use the name of the text file as a string:
# text_file = 'my_file.txt'

# Task 1:
# Count the number of units in the file.
count = 0
with open(text_file, 'r') as file:
    for string in file:            
        string_list = string.split(' ')
        for symbol in string_list:
            if int(symbol) == 1:
                count = count+1
print(count)


# Task 2:
# Find and display the 8th element of the 14th string.
# with open(text_file, 'r') as file:
#     lines = file.readlines()
#     second_line = lines[13].split(' ')
#     item = int(second_line[7])
#     print(item)


# Task 3:
# Find and display the sum of the elements in the 3rd, 6th, 9th and 12th strings.
# count = 0
# with open(text_file, 'r') as file:
#     lines = file.readlines()
#     for i in range(len(lines)):
#         string_list = lines[i].split(' ')
#         for j in range(len(string_list)):
#             if i == 2 or i == 5 or i == 8 or i == 11:
#                 count = count + int(string_list[j])
# print(count)


# Task 4 (Bonus):
# Find the sum of all the elements in the file!
# count = 0
# with open(text_file, 'r') as file:
#     lines = file.readlines()
#     for i in range(len(lines)):
#         string_list = lines[i].split(' ')
#         for j in range(len(string_list)):
#             count = count + int(string_list[j])
# print(count)


# Task 5:
# Find the sum of the maximum elements in all the strings! 
# Don't know how to find the maximum? Create an additional variable X to store the maximum. 
# Compare each element of the string to the X variable. 
# If the next string element is greater than the value of the X variable, write that string element in the X variable.
# count = 0
# max_elem = 0
# with open(text_file, 'r') as file:
#     lines = file.readlines()
#     for i in range(len(lines)):
#         string_list = lines[i].split(' ')
#         for j in range(len(string_list)):
#             if int(string_list[j]) > max_elem:
#                 max_elem = int(string_list[j])
#         count = count + max_elem
#         max_elem
# print(count)
