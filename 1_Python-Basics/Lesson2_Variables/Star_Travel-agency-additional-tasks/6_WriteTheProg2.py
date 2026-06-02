sum = int(input("Enter the sum: "))

dollar_1 = sum % 10
sum = sum // 10

dollar_10 = sum % 10
sum = sum // 10

dollar_100 = sum % 10
sum = sum // 10

dollar_1000 = sum

print(dollar_1, "- 1 dollar")
print(dollar_10, "- 10 dollar")
print(dollar_100, "- 100 dollar")
print(dollar_1000, "- 1000 dollar")