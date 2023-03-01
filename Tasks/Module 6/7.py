lst = [int(s) for s in input().split()]
for i in range(len(lst)):
    if (lst.index(lst[i]) < i):
        print("Да")
    else:
        print("Нет")