# 1 jesli 1 stu >
# 2 jesli 2 stu >
# 0 jesli ==

def f(student1,student2):
    x = student1.count("3") + student1.count("4") + student1.count("5")
    y = student2.count("3") + student2.count("4") + student2.count("5")
    if x > y:
        c = 1 
    elif x < y:
        c = 2 
    elif x == y:
        c = 0 
    return c 
    



if __name__ == "__main__":
    print(f("3,4,5","4,3"))
    print(f("3,2,5","5,5,2,5"))
    print(f("3,2,5,2,2","4,4"))