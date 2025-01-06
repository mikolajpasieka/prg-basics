def f(word):
   wave = []
   for i in range(0,len(word)):
        wave.append(word[:i].lower() + word[i].upper() + word[i+1:].lower())
   return "-".join(wave)

if __name__ == "__main__":
    print(f("book"))
    print(f("water")) 
    print(f("ok")) 
    print(f("a")) 
    print(f("")) 
