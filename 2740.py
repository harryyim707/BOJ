import sys
n, m = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
m, k = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split()))for _ in range(m)]
new_arr = [[0 for _ in range(k)]for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            new_arr[i][j] += A[i][l] * B[l][j]
for i in new_arr:
    print(*i)