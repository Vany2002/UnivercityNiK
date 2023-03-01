n = int(input())
f1 = 0
f2 = 1
p = 1
while p < n:
    f1, f2 = f2, f1 + f2
    p += 1
print(f2)