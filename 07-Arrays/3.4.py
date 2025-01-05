arr = [-15, 8, -31, 47, -2, 19]

def f(arr):
     x = arr[0]
     y = arr[0]
     for digit in arr:
          if digit < x:
               x = digit 
     for digit in arr:
          if digit > y:
               y = digit 
     return f'min: {x}, max: {y}'

    
if __name__ == "__main__":
     print(f([-15, 8, -31, 47, -2, 19]))
    
          