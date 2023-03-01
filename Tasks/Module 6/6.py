lst1 = [int(s) for s in input().split()]
lst2 = [int(s) for s in input().split()]
for i in range(len(lst1)):
    if (lst2.count(lst1[i]) > 0):
        print(lst1[i], end=' ')