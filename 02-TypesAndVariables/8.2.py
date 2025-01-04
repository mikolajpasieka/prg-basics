###
# Calculation of circle area and circumference 
#
# determine radius and PI values
r = int(input("Enter radius: "))
p = 3.14
# calculate area 
area = p * r ** 2 
# calculate circumference 
circumference = 2 * p * r 
# print results
print(f"r = {r}--> circumference = {circumference}, area = {area}")