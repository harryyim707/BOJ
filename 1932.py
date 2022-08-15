import sys
n = int(sys.stdin.readline())
tri = []
tri.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n):
    num = list(map(int, sys.stdin.readline().split()))
    added = [j for j in tri[i-1]]
    num[0] += added[0]
    num[-1] += added[-1]
    for j in range(1, len(num)-1):
        num[j] = max(num[j]+added[j-1], num[j]+added[j])
    tri.append(num)

print(max(tri[n-1]))