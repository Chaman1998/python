# Scopes and Closures in Python

## Scope
- **Definition**: The region in a program where a variable is accessible.
- **Types of Scopes**:
  1. **Local Scope**: Variables defined inside a function. Only accessible within that function.
  2. **Enclosing Scope**: Variables in the nearest enclosing function (non-local).
  3. **Global Scope**: Variables defined at the top level of a script or module. Accessible anywhere in the module.
  4. **Built-in Scope**: Reserved names in Python's built-in namespace (e.g., `len`, `print`).

### Example:
```python
x = "global"

def outer_function():
    x = "enclosing"

    def inner_function():
        x = "local"
        print(x)  # Prints "local"

    inner_function()
    print(x)  # Prints "enclosing"

outer_function()
print(x)  # Prints "global"
```
# ===============================

# Closures in Python

## What is a Closure?
- A **closure** is a function object that retains access to variables from its enclosing scope even after the scope in which it was defined has finished execution.
- It is often used to create functions with pre-configured behaviors or to maintain state across function calls.

---

## Characteristics of Closures
1. **Nested Function**: A closure must have a nested (inner) function.
2. **Referencing Variables**: The nested function must reference a variable in the enclosing (outer) function.
3. **Returning the Nested Function**: The enclosing function must return the nested function.

---

## Example of a Closure
```python
def multiplier(n):
    def inner(x):
        return x * n  # 'n' is captured from the enclosing scope
    return inner

double = multiplier(2)
print(double(5))  # Output: 10

triple = multiplier(3)
print(triple(5))  # Output: 15
```
# ===============================

# Example
```
def coder(num):
    def actual(x):
        return x ** num
    return actual

f = coder(2)

print(f(3))
```

## Output
```
9
```
** Here f() refer to the 'actual(x)', and the 'f = coder()' value refer to the 'num'.

