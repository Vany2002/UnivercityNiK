N = int(input())
f = {}
for i in range(N):
    line = input().split()
    f[line[0]] = line[1:]
k = int(input())
result = []
for i in range(k):
    line = input().split()
    given = str(f[line[1]]).replace('R', 'read').replace('W', 'write').replace('X', 'execute')
    if given.__contains__(line[0]):
        result.append('OK')
    else:
        result.append('Denied')
print(*result, sep='\n')