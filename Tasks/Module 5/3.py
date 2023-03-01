x = int(input())
y = int(input())
d = 1
while x < y:
    d = d + 1
    x = x + (10 * x)/100
print(d)