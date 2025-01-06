def f(vname):
    import re
    pattern = "^[a-zA-Z_][a-zA-Z0-9_]{0,4}$"
    if re.match(pattern,vname):
        return True 
    else:
        return False
    
if __name__ == "__main__":
    print(f("abc"))
    print(f("Abc") ) 
    print(f("aBC")) 
    print(f("aBC"))  
    print(f("abcdef"))
    print(f("8abc")) 
    print(f("_aB8_")) 
    print(f("_4x"))  