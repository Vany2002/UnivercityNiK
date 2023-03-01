a = int(input())
k = 0
while a != 0:
    b = int(input())
    if (b != 0) and (a < b):
        k = k + 1
    a = b
print(k)