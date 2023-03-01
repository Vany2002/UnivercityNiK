lst = [int(s) for s in input().split()]
for i in lst:
    if int(i) % 2 == 1:
        print(i, end=' ')