def f(vname):
    import  re
    pattern = "^[a-zA-Z_][a-zA-Z0-9_]{1,4}$"
    if re.match(pattern, vname):
        return True
    return False

if __name__ == "__main__":
    print(f("Abc"))
    print(f("aBC"))
    print(f("_ab_c"))
    print(f("abcdef"))
    print(f("8abc"))
    print(f("_aB0_"))
    print(f("__4x"))