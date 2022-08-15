import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
r_dp = [0] * n
l_dp = [0] * n
result = [0] * n
for i in range(n):
    r_dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i] and r_dp[i] < r_dp[j]+1:
            r_dp[i] = r_dp[j]+1
for i in range(n-1, -1, -1):
    l_dp[i] = 1
    for j in range(n-1, i, -1):
        if arr[j] < arr[i] and l_dp[i] < l_dp[j]+1:
            l_dp[i] = l_dp[j]+1
for i in range(n):
    result[i] = r_dp[i] + l_dp[i] - 1
print(max(result))