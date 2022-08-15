import sys
n, k = map(int, sys.stdin.readline().split())
dp = dict()
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    if i in dp:
        continue
    else:
        dp[i] = dp[i-1] * i
print(dp)
result = (dp[n] // (dp[k] * dp[n-k])) % 10007
print(result)