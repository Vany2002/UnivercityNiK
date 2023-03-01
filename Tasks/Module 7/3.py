N = int(input())
w = {}
for i in range(N):
    line = input().split()
    if not line[0] in w:
        w[line[0]] = 0
    w[line[0]] += int(line[1])
print(w)