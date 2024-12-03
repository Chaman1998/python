>>> username = "Helloworld"

>>> len(username)

10

>>> username[0]

'H'

>>> username[0] = 'A'

Traceback (most recent call last):
    File "\<stdion>", line 1, in \<module>
    
TypeError: 'str' object does not support item assignment

>>> username[-1]

'd'

>>> username[1:3]

'el'

>>> dir(username)

============================================

>>> mylist = [123, "chai", 3.14]

>>> mylist

[123, "chai", 3.14]

>>> len(mylist)

3

>>> mylist[0]

123

============================================

>>> myD = {'one': 'lemon', 'two': 'ginger', 'comic': 'naagraj'}

>>> myD

{'one': 'lemon', 'two': 'ginger', 'comic': 'naagraj'}

>>> myD['comic']

'naagraj'

>>> muD['comics']

Traceback (most recent call last):
    File "\<stdion>", line 1, in \<module>
    
KeyError: 'comics'

============================================
>>>myTup = (1, 2, 3)

>>>myTup[0]

1

>>> len(myTup)

3
============================================