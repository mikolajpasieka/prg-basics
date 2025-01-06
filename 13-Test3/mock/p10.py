def f(d):
    count = 0 
    total = 0
    count1 = 0 
    for value1 in d.values():
        total += value1
        count1 += 1 
    
    x = total/count1

    for value in d.values():
        if value > x :
            count += 1 
    
    return count 

if __name__ == "__main__":
    print(f({"LO231":150,"BA787":120,"NZ15":30}))
    print(f({"LO231":150,"BA787":20,"NZ15":30})) 
