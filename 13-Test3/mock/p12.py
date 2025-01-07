class C:
    def __init__(self,xvalue,yvalue):
        self.xvalue = xvalue
        self.yvalue = yvalue

    def m1(self):
        if self.xvalue == 0 or self.yvalue ==0:
            return 0
        return 1
    
    def m2(self,a,b):
        if a > 0 and self.xvalue > 0 and b > 0 and self.yvalue > 0:
            return True
        elif a < 0 and self.xvalue < 0 and b > 0 and self.yvalue > 0:
            return True
        elif a < 0 and self.xvalue < 0 and b < 0 and self.yvalue < 0:
            return True
        elif a > 0 and self.xvalue > 0 and b > 0 and self.yvalue > 0:
            return True
        return False
    
    def m3(self,a,b):
        if (((a - self.xvalue )**2) + ((b - self.yvalue)**2 ))**0.5 > 5:
            return True
        return False
    
def main():
    p = C(2,3)
    print(p.m1())
    print(p.m2(7,4))
    print(p.m2(-3,1))
    print(p.m3(8,5))
    print(p.m3(4,7))

    p1 = C(0,5)
    print(p1.m1())
    print(p1.m2(4,7))
    print(p1.m3(-7,0))


if __name__ == "__main__":
    main()
