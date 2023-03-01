x = int(input())
n = 0
while 2 ** n <= x:
    n = n + 1
n = n - 1
print(n, 2 ** n)
