word = input()
if word.count('f') == 1:
    print(word.find('f'))
elif word.count('f') > 1:
    print(word.find('f'), word.rfind('f'))
else:
    print("-1")



