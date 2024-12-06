age = int(input("Provide me an age: "))
day = "Wednessday"

price = 12 if age >= 18 else 8

if day == "Wednessday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $", price)