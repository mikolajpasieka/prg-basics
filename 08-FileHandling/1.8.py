with open('pets.txt') as file:
    content = file.read()
    lines = content.splitlines()

    for line in lines:
        print(line)

    n = len(content.split())
    
    print(n)