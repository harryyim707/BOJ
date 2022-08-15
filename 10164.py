import sys
n, m, k = map(int, sys.stdin.readline().split())
dp = [[1 for _ in range(m+1)] for _ in range(n+1)]
col = k % m
row = k // m
if col:
    row += 1
else:
    col = m
for i in range(2, n+1):
    for j in range(2, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
if k == 0 or k == n*m:
    print(dp[n][m])
else:
    print(dp[row][col]*dp[n-row+1][m-col+1])