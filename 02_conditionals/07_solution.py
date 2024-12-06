order_size = input("Coffee order: 's' for 'Small', 'm' for 'Medium', or 'l' for  'Large': ")
extra_shot = input("'t' for 'Extra shot' of espresso or 'f': ")

if order_size == 's':
    size = "Small"
elif order_size == 'm':
    size = "Medium"
elif order_size == 'l':
    size = "Large"

if extra_shot == 't':
    extra = "extra sort"
else:
    extra = "without extra sort"

print(size + " size of coffee with " + extra)