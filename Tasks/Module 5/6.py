n = int(input())
f1 = 0
f2 = 1
p = 1
while f2 <= n:
    if f2 == n:
        print(p)
        break
    f1, f2 = f2, f1 + f2
    p += 1
else:
    print(-1)

