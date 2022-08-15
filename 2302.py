dp = [0 for _ in range(41)]
ans = 1
mid = 0
N = int(input())
M = int(input())
dp[0] = 1
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]
for _ in range(M):
    vip = int(input())
    ans *= dp[vip-1-mid]
    mid = vip
ans *= dp[N-mid]
print(ans)