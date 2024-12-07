import math
number = int(input("Enter the number for check the prime: "))

if number <= 1:
    print("This is not a prime number.")
else:
    for i in range(2, number):
        if (number % i) == 0:
            print("This is not a prime number.")
            break
        else:
            print("This is a prime number.")
            break