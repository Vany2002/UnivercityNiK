a = int(input())
pr = -1
psl = 0
mx = 0
while a != 0:
    if a == pr:
        psl += 1
    else:
        pr = a
        mx = max(mx, psl)
        psl = 1
    a = int(input())
print(mx)


