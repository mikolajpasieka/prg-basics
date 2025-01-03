def f(hours,minutes,seconds):
    if minutes == hours*60 and seconds == hours*60*60:
        x = True
    else: 
        x = False
    return x



if __name__ == "__main__":
    print(f(1,60,3600))
    print(f(2,120,7200))
    print(f(4,220,14400))
    print(f(3,180,10600))