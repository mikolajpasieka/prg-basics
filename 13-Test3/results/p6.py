def f(fnc,res):
    resoults = list(filter(fnc,res))
    return max(resoults) - min(resoults)
if __name__ == "__main__":
    res = [95,90,20,50,70]
    fnc1 = lambda x: x >50
    fnc2 = lambda x : x>30 and x <90
    print(f(fnc1,res))
    print(f(fnc2,res))