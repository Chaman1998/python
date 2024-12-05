>>> tea_varities = ["Black", "Green", "OOlong", "White"]
>>> tea_varities

["Black", "Green", "Oolong", "White"]

>>> print(tea_varities)

['Black', 'Green', 'Oolong', 'White']

>>> print(tea_varities[0])

Black

>>> print(tea_varities[1])

Green

>>> print(tea_varities[-1])

White

>>> print(tea_varities[1:3])

['Green', 'Oolong']

>>> print(tea_varities[:2])

['Black', 'Green']

>>> print(tea_varities[2:])

['Oolong', 'White']

>>> tea_varities[3] = "Herbal"
>>> print(tea_varities)

['Black', 'Green', 'Oolong', 'Herbal']
==============================================================

        Error Part
>>> tea_varities[1:2] = "Lemon"
>>> tea_varities
'['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']

---------------------------------------

        Right Part
>>> tea_varities[1:2] = ["Lemon"]
>>> tea_varities

['Black', 'Green", 'Oolong', 'Herbal']

==============================================================

>>> tea_varities.append("Masala")
>>> if "Masala" in tea_variables:
...    print("I have Masala Tea.")

I have Masala Tea.

>>> tea_varities.pop()

'Masala'

>>> tea_varities.remove("Green")
>>> tea_varities

['Black', 'Green", 'Oolong', 'Herbal']

