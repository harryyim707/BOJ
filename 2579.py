import sys
n = int(sys.stdin.readline())
stairs = []
dp = []
for _ in range(n):
    stairs.append(int(sys.stdin.readline()))

dp.append(stairs[0])
dp.append(max(stairs[0]+stairs[1], stairs[1]))
dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))

for i in range(3, n):
    dp.append(max(dp[i-2]+stairs[i], dp[i-3]+stairs[i]+stairs[i-1]))

print(dp[n-1])