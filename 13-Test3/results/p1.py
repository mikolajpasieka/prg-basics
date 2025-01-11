def f(d):
    count = 0
    for x in d:
        if x == "+":
            count +=1
        if x == "-":
            count -= 1 
    return count 
if __name__ == "__main__":
    print(f(""))
    print(f("+-+"))
    print(f("+-+++-+---"))
    print(f('+-+++++-'))