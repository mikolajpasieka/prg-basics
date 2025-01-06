paragraph = "cat dog mouse cat rat cat mouse"

text_splited = paragraph.split()
text_splited_once = set(text_splited)
dict = {}

for x in text_splited_once:
    dict[x] = text_splited.count(x)

print(dict)