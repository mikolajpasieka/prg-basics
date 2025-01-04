h = int(input('Enter number of hours of parking:'))
if h <= 2:
    x = h*5
elif h > 2 and h <=6:
    x = 10 + (h-2)*15
elif h > 6:
    x = 70 + (h-6)*20
print(x)