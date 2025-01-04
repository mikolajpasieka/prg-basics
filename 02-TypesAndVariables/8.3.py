###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# determine temperature in degrees Celsius
c = float(input("Enter temperature in degrees Celsius: "))
# convert temperature to degrees Fahrenheit and Kelvin
f = c * 9 / 5 + 32 
k = c + 273.15
# print the results 
print(f"{c} degrees Celsius is equal to {f} degrees Fahrenheit and {k} Kelvin")