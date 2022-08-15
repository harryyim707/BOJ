import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
arr = [0 for _ in range(n)]
arr[0] = num[0]
for i in range(n):
    arr[i] = arr[i-1] + num[i]
ans = 0
#case 1 bee < honey < bee
for i in range(1, n):
    temp = arr[i]-arr[0]+arr[-2]-arr[i-1]
    ans = max(ans, temp)

#case 2 honey < bee < bee
for i in range(1, n-1):
    temp = arr[n-2] - arr[i] + 2 * (arr[i-1])
    ans = max(ans, temp)

#case 3 bee, bee < honey
for i in range(1, n):
    temp = arr[i-1] - arr[0] + 2*(arr[-1]-arr[i])
    ans = max(ans, temp)
print(ans)