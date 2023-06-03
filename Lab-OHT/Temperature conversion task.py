def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

# Examples:
celsius = 32
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius = {fahrenheit} degree Fahrenheit.")

kelvin = celsius_to_kelvin(celsius)
print(f"{celsius} degrees Celsius  = {kelvin} Kelvin.")

# You can also convert directly between  Fahrenheit and Kelvin:
fahrenheit = 45
kelvin = fahrenheit_to_kelvin(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit = {kelvin} Kelvin.")

 




