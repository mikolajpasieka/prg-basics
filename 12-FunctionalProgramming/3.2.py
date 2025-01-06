sentence = 'I completely agree with you'
result = list(map(lambda x: len(x) , sentence.split()))
print('Text:', sentence)
print('No. of letters in words:', end= " ")
print(result)