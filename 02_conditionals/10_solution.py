# Recommend a type of pet food based on the pet's species and age. 
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = input("Select pet ('d' for Dog and 'c' for Cat: ").lower()


if pet == 'd':
    age = int(input("Enter the age of the pet: "))
    if age < 2:
        print("Puppy Foot")
    else:
        print("Adult Foot")
elif pet == 'c':
    age = int(input("Enter the age of the pet: "))
    if age < 5:
        print("Junior cat Foot")
    else:
        print("Senior cat Foot")
else:
    print("Please select Pet carefully")