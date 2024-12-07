# import time
# print("Code is here")
# username = "Hello"
# print(username)

lst = [1, 2, 3]          # List is iterable but not an iterator
print(iter(lst) is lst)  # False
it = iter(lst)           # Create an iterator from the list
print(next(it))          # 1
print(next(it))          # 2
