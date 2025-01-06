translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
word = input('Enter word to translate: ')
if word in translations.keys():
    print(translations[word])
else:
    print('Translation unavailable')

