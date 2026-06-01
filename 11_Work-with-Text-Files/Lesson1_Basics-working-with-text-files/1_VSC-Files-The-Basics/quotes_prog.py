# fix if the text file cannot be found even if it is in the same folder as the script
# this happens when the terminal does not point specifically to the folder where the script is located, but to a parent folder
from pathlib import Path
quotes_file = Path(__file__).with_name("quotes.txt")
    
# if the terminal points directly to the folder where the script and text file are located, use
# quotes_file = "quotes.txt"
with open(quotes_file, "r", encoding = "UTF-8") as file:
    for line in file:
        print(line)


author = input("Who wrote these lines? ")
with open(quotes_file, "a",  encoding = "UTF-8") as file:
    file.write("("+author+")"+"\n")


while True:
    answer = input("Want to add another quote? (yes/no)")
    answer = answer.lower()
    if answer == "yes":
        quote = input("Enter a quotes: ")
        author = input("Enter an author: ")
        file = open(quotes_file, "a",  encoding = "UTF-8")
        file.write(quote+"\n"+"("+author+")"+"\n")
        file.close()
    else:
        break


with open(quotes_file, "r", encoding = "UTF-8") as file:
    for line in file:
        print(line)
