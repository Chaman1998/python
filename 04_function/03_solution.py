def multiply(p1, p2):
    return p1 * p2

# Input values from the user
n1 = input("Enter the First input: ")
n2 = input("Enter the Second input: ")

# Function to check if a value is an integer
def is_integer(value):
    try:
        # Try converting the value to an integer
        int(value)
        return True
    except ValueError:
        return False

# Checking the conditions
if is_integer(n1) and is_integer(n2):
    # Both inputs are integers
    p1 = int(n1)
    p2 = int(n2)
    result = multiply(p1, p2)
    print("Both are integers. Result:", result)

elif is_integer(n1) or is_integer(n2):
    # One input is an integer and the other is a string
    if is_integer(n1):
        p1 = int(n1)
        p2 = n2  # n2 should be a string
    else:
        p1 = int(n2)
        p2 = n1  # n1 should be a string
    result = multiply(p1, p2)
    print("One input is integer and other is string. Result:", result)

else:
    print("Must have one integer input")
