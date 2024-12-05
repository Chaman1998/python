>>> chai_types = {"Masala", "Spice", "Ginger", "Zesty", "Green", "Mild"}
>>> chai_types

{"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

>>> chai_types["Masala"]

'Spicy'

>>> chai_types.get("Genger")

'Zesty'

>>> for chai in chai_types:
...     print(chai)
...

Masala
Ginger
Green

>>> for chai in chai_types:
...     print(chai, chai_types[chai])
...

Masala Spicy
Ginger Zesty
Green Mild

>>> for key, value in chai_types.items():
...     print(key, value)
...

Masala Spicy
Ginger Zesty
Green Mild

***
pop()   --remove the selected item
    Ex: -   pop('name of the key')

popitem()   --remove the last item

***
copy()
    Ex: -   new_chai_test = chai_types.copy()

***

========================================================

>>> tea_shop = {
    ... "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    ... "tea": {"Green": "Mild", "Black": "Strong"}
}

>>> tea_shop

{"chai": {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'tea': {'Green': 'Mild', 'Black': 'Strong'}}

>>> print(tea_shop)

{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'tea': {'Green': 'Mild', 'Black': 'Strong'}}

>>> tea_shop["chai"]

{'chai': 'Masala': 'Spicy', 'Ginger': 'Zesty'}

>>> tea_shop["chai"]["Ginger"]

'Zesty'

==========================================================

>>> squared_num = {x:x**2 for x in range(6)}
>>> squared_num

{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

>>> squared_num.clear()

{}

==========================================================

