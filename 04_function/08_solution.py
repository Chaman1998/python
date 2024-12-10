# **kwargs

# def print_kwargs(name, power):
#     print("Name:",name, "Power:",power)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "Shaktiman", power = "Lazer")
print_kwargs(name = "Shaktiman")
print_kwargs(name = "Shaktiman", power = "Lazer",enemy = "Dr. Jackaal")
