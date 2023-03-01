lst = input()
first = lst.find('h')
last = lst.rfind('h')
print(f'{lst[:first+1]}{lst[first+1:last].replace("h", "H")}{lst[last:]}')