def f(detector):
    total = 0 
    total_max = 0 
    for char in detector:
        if char == "+":
            total += 1 
        if char == "-":
            total -= 1 
        total_max = max(total_max, total)
    return total_max >= 3
           
if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))