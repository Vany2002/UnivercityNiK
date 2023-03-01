lst = input().split()
w = {}
for i in range(len(lst)):
    if not lst[i] in w:
        w[lst[i]] = 0
    print(w[lst[i]], end=' ')
    w[lst[i]] += 1