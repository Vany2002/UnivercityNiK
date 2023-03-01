lst = [int(s) for s in input().split()]
for i in range(len(lst) - 1):
    if lst[i] < lst[i + 1]:
        print(lst[i + 1], end=' ')