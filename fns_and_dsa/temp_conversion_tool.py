FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit-32 )*FAHRENHEIT_TO_CELSIUS_FACTOR
    print (f"{fahrenheit}°F is {celsius}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    print(f"{celsius}°C is {fahrenheit}°F")



value = int(input('Enter the temperature to convert: '))
unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ') 

if unit.lower() == "f":
    convert_to_celsius(value)
elif unit.lower() == "c":
    convert_to_fahrenheit(value)
else : 
    print("you entered a wrong unit !")         