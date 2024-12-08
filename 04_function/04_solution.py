import math

def circle_redius(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

radius = int(input("Enter circle redius: "))

area, circumference = circle_redius(radius)
print("Area:",area,"circumference:",circumference)