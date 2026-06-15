start = int(input("The year of entering the partnership with the fund: "))
end = int(input("The year of ending the partnership with the fund: "))
for year in range(start, end+1):
    if year%2 == 0:
        print(year, "- a series of conferences and round tables with experts.")
    else:
        print(year, "- the Startup of the Year international competition.")
