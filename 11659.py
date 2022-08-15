import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n+1)
for i in range(n):
    dp[i+1] = dp[i] + num[i]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j]-dp[i-1])