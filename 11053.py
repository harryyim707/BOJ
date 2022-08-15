import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
print(max(dp))