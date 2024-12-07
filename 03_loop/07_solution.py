print(" -:Enter the number between 1 - 10:- ")

while True:
    number = int(input("Enter the number: "))
    if 1<= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number.")