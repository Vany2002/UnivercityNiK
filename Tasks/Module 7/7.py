N = int(input())
w = {}
for i in range(N):
    line = input().split()
    for i in range(len(line)):
        if not line[i] in w:
            w[line[i]] = 0
        w[line[i]] += 1
result = []
for key, value in w.items():
    result.append(f'{value} {key}')
result.sort()
result.reverse()
for i in range(len(result)):
    line = result[i].split()
    print(f'{line[1]} {line[0]}')