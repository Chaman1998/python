input_str = input("Enter the string: ")

print(input_str.count('r'))

for char in input_str:
    if input_str.count(char) == 1:
        print("Char is: ",char)