###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
print(f"volume = {int(a)*int(b)*int(c)}, surface area = {2*(int(a)*int(b)+int(a)*int(c)+int(b)*int(c))}")