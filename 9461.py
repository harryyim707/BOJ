import sys
t = int(sys.stdin.readline())
dp = {1:1, 2:1, 3:1, 4:2, 5:2}
def cal(x):
    if x in dp:
        return dp[x]
    dp[x] = cal(x-1)+cal(x-5)
    return dp[x]


for _ in range(t):
    n = int(sys.stdin.readline())
    print(cal(n))
