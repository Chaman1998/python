-: Iteration tool :-
(For, Comprehension)
    |       |
    |       |
    |     -: Iterable Objects :-
    |     (lists, file)
    |       |
    |       |
    v       v
-:              :-
__next__

===============================================

-:  File Read every line  :-

f = open('test.py')
f.readline()

or,

f = open('test.py')
f.__next__()

But here show the "StopIteration" in the end.

------------------------------------------

-:  File Read with For Loop :-

for line in open('test.py'):
...     print(line)

or,
for line in open('test.py'):
...     print(line, end='') 

------------------------------------------

-:  File Read with While Loop :-

f = open('test.py')
while True:
...     line = f.readline()
...     if not line: break
...     print(line,end='')

------------------------------------------

>>> myList = [1, 2, 3, 4]
>>> I = iter(myList)
>>> I

<list_iterator object at 0x10...>

>>> I.__next__()

1

===============================================

# Key Concepts: Iterators vs Iterables

## Iterable:
- An object is **iterable** if it can return an iterator using the `iter()` function.
- **Examples:** Lists, tuples, dictionaries, strings, etc.
- These objects implement the `__iter__()` method but are **not iterators themselves**.

## Iterator:
- An object is an **iterator** if it implements the `__iter__()` and `__next__()` methods.
- Iterators are objects that produce items one at a time when you call `next()` on them.
- **Examples:** File objects, generators, etc.

===============================================

# Key Concepts: Iterators vs Iterables

## Iterable:
- An object is **iterable** if it can return an iterator using the `iter()` function.
- **Examples:** Lists, tuples, dictionaries, strings, etc.
- These objects implement the `__iter__()` method but are **not iterators themselves**.

### For Dictionaries:
- A dictionary is **iterable** and returns its **keys** by default when used in a `for` loop or with `iter()`.
- Example:
  ```python
  my_dict = {'a': 1, 'b': 2}
  for key in my_dict:
      print(key)  # Outputs: 'a', 'b'
