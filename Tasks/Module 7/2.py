N = int(input())
w = {}
for i in range(N):
    line = input().split()
    w[line[0]] = line[1]
rv = input()
for i in w:
    if w[i] == rv:
        print(i)
        break