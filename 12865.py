import sys
n, k = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(k+1)] for _ in range(n)]
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    for index in range(1, k+1):
        if index >= w:
            arr[i][index] = max(arr[i-1][index], arr[i-1][index-w]+v)
        else:
            arr[i][index] = arr[i-1][index]
print(max(arr[-1]))