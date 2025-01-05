arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

def f(arr):
    x = len(arr[0])
    for name in arr:
        if len(name) > x:
            y = name 
            x = len(name)
    return y 

print('Names: Genowefa Onufry Celestyna Alojzy Pankracy')
print('Longest name:', f(arr))