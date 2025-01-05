def f(text):
    if len(text) == 0: 
        return ""
    if len(text) == 1:
        return text
    if len(text) > 1:
        text1 = text[0]
        for i in range(1,len(text)):
            text1 = text1 + "-" + text[i]     
    return text1 

if __name__ == "__main__":
    print(f("Univesity"))
    print(f("UE"))
    print(f("x"))
    print(f(""))