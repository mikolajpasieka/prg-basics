#The distance to the horizon depends on the height of the observer above the ground. 
# The higher you are, the farther away the horizon is. 

# For most situations, you can use the following formula:
# d = 3.57 × √h
# Where:
# d is the distance to the horizon in kilometers
# h is the height of the observer in meters

# Write a program that calculates the distance to the horizon 
# from a height given in meters from the keyboard. Then, using the program, calculate the distance to the horizon in km when:
# 1. You are standing on a beach, by the sea, on the water line (calculate the distance for your height in m). 
# You have probably been to the seaside many times. 
# Can you believe that the horizon is only a few kilometers away?
# 2. You are looking out of a hotel window located by the sea, the window is at a height of 20 meters.

def f(h):
    if  h == 0 :
        h1 = h + 1.73
    else:
        h1 = h 
    return round(3.57 * (h1 ** 0.5),2)


if __name__ == "__main__":
    print(f(0))
    print(f(20))