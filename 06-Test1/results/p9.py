def f(sizes):
    x = str(sizes)
    s = x.count("S")
    m = x.count("M")
    l = x.count("L")
    if s < m and s < l:
        y = "S"
    elif m < s and m < l:
        y = "M"
    elif l < s and l < m:
        y = "L"
    elif s == m and s< l and m < l:
        y = "S"
    elif s == l and s< m and l < m:
        y = "S"
    elif l == m and l < s and m < s:
        y = "M"
    return y 




if __name__ == "__main__":
    print(f("L,S,L,M,L,S,S,L"))
    print(f("M,L,L,L,M"))
    print(f("M,L,M,L,S,S,S"))