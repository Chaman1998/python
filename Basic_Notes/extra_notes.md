# Key Concepts for Checking Numbers in Python

---

## 1. `isinstance()`
- **Definition**: Checks if an object is an instance of a specific type or class.
- **Use Case**: To verify if a variable is of a particular data type (e.g., `int`, `float`).

### Example:
```python
num = 10
if isinstance(num, int):
    print(f"{num} is an integer.")
else:
    print(f"{num} is not an integer.")
```

`Output:`
10 is an integer.

===================================================

# Understanding `isdigit()` in Python

---

## `isdigit()`
- **Definition**: A string method that checks if all characters in a string are numeric digits (0-9).
- **Use Case**: Useful for validating if a string can represent a positive integer (does not account for negative numbers or decimals).

---

## Key Points:
1. It works only on strings.
2. Returns `True` if all characters are digits; otherwise, returns `False`.
3. Does not validate strings with negative signs or decimal points.

---

## Example:

```python
# Example 1: Valid Numeric String
num = "123"
if num.isdigit():
    print(f"{num} is a valid number.")
else:
    print(f"{num} is not a valid number.")

# Example 2: Non-Numeric String
num = "123a"
if num.isdigit():
    print(f"{num} is a valid number.")
else:
    print(f"{num} is not a valid number.")
```

`Output:`

- 123 is a valid number.
- 123a is not a valid number.


`Limitations:`

**It does not handle:**
- Negative numbers ("-123".isdigit() → False)
- Floating-point numbers ("12.3".isdigit() → False)

===================================================

# Understanding `try-except` in Python for Number Validation

---

## `try-except` Block
- **Definition**: A control flow mechanism used to handle errors or exceptions in Python code, allowing the program to continue executing even if an error occurs.
- **Use Case**: Commonly used for handling type conversion (like converting a string to a number) and catching errors that may arise.

---

## Key Points:
1. The `try` block contains the code that may raise an exception.
2. The `except` block contains the code that handles the exception if one occurs.
3. You can handle specific exceptions or use a general `except` for all exceptions.

---

## Example 1: Using `try-except` to Check if Input is a Number

```python
# Example: Handling invalid input using try-except
num_str = input("Enter a number: ")

try:
    num = int(num_str)  # Attempt to convert the input to an integer
    print(f"The number is {num}")
except ValueError:
    print("That's not a valid number!")
```

`Output:`

- If the input is a valid integer (e.g., 42), it prints: The number is 42
- If the input is non-numeric (e.g., "abc"), it prints: That's not a valid number!

