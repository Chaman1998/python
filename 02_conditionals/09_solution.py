year = int(input("Enter the year: "))

if (year % 400 == 0) or (year % 4 == 0  and year % 100 != 0):
    print(year,"Leap Year.")
else:
    print(year,"is not Leap Year.")
