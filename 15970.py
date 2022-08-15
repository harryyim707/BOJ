import sys
n = int(sys.stdin.readline())
info = []
for _ in range(n):
    info.append(list(map(int, sys.stdin.readline().split())))
m = max(info)
d = [100000 for _ in range(m[0]+1)]
for i in range(n):
    for j in range(n):
        if info[i][1] == info[j][1] and i != j:
            d[info[i][0]] = min(d[info[i][0]], abs(info[i][0]-info[j][0]))
sum = 0
for i in d:
    if i != 100000:
        sum += i
print(sum)