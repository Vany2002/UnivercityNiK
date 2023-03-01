N = int(input())
w = {}
for i in range(N):
    line = input().split()
    for j in range(len(line)):
        if not line[j] in w:
            w[line[j]] = 0
        w[line[j]] += 1
max = 1
w1 = {}
for i in w:
    if w[i] > max:
        max = w[i]
for i in w:
    if w[i] == max:
        w1[i] = w[i]
w1 = dict(sorted(w1.items()))
for i in w1:
    print(i)
    break