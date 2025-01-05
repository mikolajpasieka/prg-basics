def number(text):
    count = 1 
    for char in text:
        if char == " ":
            count += 1 
    return count 


def longest(text):
    words = text.split()
    words.sort(key=len, reverse=True)
    return words
 
def alphabetical(text):
    words = text.split()
    words.sort()
    return words
