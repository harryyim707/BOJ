from operator import index


n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
for i in range(n-1, -1, -1):
    dp[i] = 1
    for j in range(n-1, i, -1):
        if arr[j] < arr[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
print(max(dp))
