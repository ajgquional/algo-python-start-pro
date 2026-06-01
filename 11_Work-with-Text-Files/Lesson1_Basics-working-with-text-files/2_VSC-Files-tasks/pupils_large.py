import time
class Pupil:
    def __init__(self, Surname, Name, Mark):
        self.Surname = Surname
        self.Name = Name
        self.Mark = Mark

Pupils_amount = 0
Best_pupils = []
Sum = 0

current_amount = 0
start_time = time.time()

# fix if the text file cannot be found even if it is in the same folder as the script
# this happens when the terminal does not point specifically to the folder where the script is located, but to a parent folder
from pathlib import Path
pupils_large_file = Path(__file__).with_name("pupils_large.txt")
# if the terminal points directly to the folder where the script and text file are located, use
# pupils_large_file = "pupils_large.txt"
with open(pupils_large_file, "r", encoding = "utf-8") as file:
    for line in file:
        data = line.split(" ")
        data_pupil = Pupil(data[0], data[1], int(data[2]))

        if data_pupil.Mark == 5:
            Best_pupils.append(data_pupil.Surname)
        Pupils_amount += 1 
        Sum += int(data_pupil.Mark)

        current_amount += 1

print("Average grade:", (Sum/Pupils_amount), "\n\nTop 10 students:")
for pupil in Best_pupils[0:10]:
     print(pupil)

print("Runtime: ", (time.time()-start_time), "seconds")
