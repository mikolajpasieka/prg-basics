def f(number,x,y):
    if number >= x and number <= y:
        result = True
    elif number < x or number > y: 
        result = False
    if result == True:
        return "yes"
    elif result == False:
        return "no"