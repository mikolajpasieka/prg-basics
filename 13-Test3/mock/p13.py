def f(mnumbers):
    import re
    pattern = "^[+-]?[a-dA-D1-7]+$"
    count = 0 
    for m in mnumbers:
        if re.match(pattern, m):
            count += 1
     
    return count 

if __name__ == "__main__":
    print(f(["A15","-31","7abC","+D1","-gH"]))
    print(f(["A05","-3+1","7ab8C","+D1","-22k"])) 