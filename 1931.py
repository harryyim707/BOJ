import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    arr.append((start, end))
arr.sort(key=lambda x : (x[1], x[0]))
cnt = 1
prev = arr[0][1]
for i in arr[1:]:
    if prev<=i[0]:
        prev = i[1]
        cnt+=1
print(cnt)