x = int(input())
n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
tot = 0
for elem in arr:
    tot += elem[0]*elem[1]
if tot == x:
    print('Yes')
else:
    print('No')