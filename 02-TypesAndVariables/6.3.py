###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
list = university.split()
x= ""
for i in list:
    if len(i) > 2:
        x = x + i[0]

print(x)