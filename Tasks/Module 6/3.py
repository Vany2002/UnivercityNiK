lst = [int(s) for s in input().split()]
for i in range(len(lst)):
    if (i % 2 == 1):
        lst[i-1], lst[i] = lst[i], lst[i-1]
print(*lst)