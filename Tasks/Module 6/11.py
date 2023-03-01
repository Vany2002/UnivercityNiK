lst = input()
first = lst.find('h')
last = lst.rfind('h')
print(f'{lst[:first]}{lst[last:first:-1]}{lst[last:]}')