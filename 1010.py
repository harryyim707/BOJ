import sys
t = int(sys.stdin.readline())
dp = dict()
dp[0] = 1
dp[1] = 1


def fac(x):
    if x in dp:
        return dp[x]
    else:
        dp[x] = fac(x-1) * x
        return dp[x]


for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    result = fac(m) // (fac(n)*fac(m-n))
    print(result)