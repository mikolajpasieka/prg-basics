def f(x,y):
    if x == 0 and y == 0:
        return f"Point P({x},{y}) is located in the position (0,0) of the coordinate system"
    elif x > 0 and y >0:
        return f"Point P({x},{y}) is in the first quadrant of the coordinate system"
    elif x < 0 and y > 0:
        return f"Point P({x},{y}) is in the second quadrant of the coordinate system"
    elif x < 0 and y < 0:
        return f"Point P({x},{y}) is in the third quadrant of the coordinate system"
    elif x > 0 and y < 0:
        return f"Point P({x},{y}) is in the fourth quadrant of the coordinate system"
    elif x == 0 and y != 0:
        return f"Point P({x},{y}) is on the y-axis"
    elif x != 0 and y == 0:
        return f"Point P({x},{y}) is on the x-axis"
    else: 
        return "Invalid point"
    
if __name__ == "__main__":
    print(f(0,0))
    print(f(5,2))
    print(f(-5,2))
    print(f(-5,-2))
    print(f(5,-2))
    print(f(0,2))
    print(f(5,0))
    