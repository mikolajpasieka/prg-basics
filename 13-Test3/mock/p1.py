def f(word):
    wave = []
    a = len(word)
    if a == 0:
        return ''
    if a == 1:
        return word.upper()
    for i in range(0,a):
        wave.append(word[:i] + word[i].upper() + word[i+1:].lower())
                
    return "-".join(wave)
    

if __name__ == "__main__":
    print(f("book"))
    print(f("water")) 
    print(f("ok")) 
    print(f("a")) 
    print(f("")) 