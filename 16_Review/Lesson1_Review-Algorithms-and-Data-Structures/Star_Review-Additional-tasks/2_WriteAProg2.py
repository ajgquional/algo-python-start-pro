total = int(input('Initial price of AlgoCoin: '))
day1 = int(input('Price change for day 1 (%): '))
day2 = int(input('Price change for day 2 (%): '))
day3 = int(input('Price change for day 3 (%): '))

end_day1 = total*(1+day1/100)
end_day2 = end_day1*(1+day2/100)
end_day3 = end_day2*(1+day3/100)

print('After the first day, the price was:', round(end_day1,3))
print('After the second day, the price was:', round(end_day2,3))
print('After the third day, the price was:', round(end_day3,3))
