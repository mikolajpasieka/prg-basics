def f(name):
    a = len(name)
    if name[a-1] == 'a':
        return f"{name} -- Polish female name"

if __name__ == '__main__':
    print(f('Anna'))
    print(f('Jonna'))
    print(f('Ilona'))
    print(f('Lucyna'))
    print(f('Katarzyna'))