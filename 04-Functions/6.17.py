def f(palindrome):
    a = len(palindrome)
    for i in range(0,a):
        if palindrome[i] == palindrome[a-i-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    print(f("radar")) 
    print(f("12-11-21")) 
    print(f("book")) 

 