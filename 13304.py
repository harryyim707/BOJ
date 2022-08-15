import sys
N, K = map(int, sys.stdin.readline().split())
s = [0, 0, 0, 0, 0] #12남여, 34여, 34남, 56여, 56남

for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    if Y == 1 or Y == 2:
        s[0] += 1
    if S == 0 and (Y == 3 or Y == 4):
        s[1] += 1
    if S == 1 and (Y == 3 or Y == 4):
        s[2] += 1
    if S == 0 and (Y == 5 or Y == 6):
        s[3] += 1
    if S == 1 and (Y == 5 or Y == 6):
        s[4] += 1
ans = 0
for i in s:
    if i % K != 0:
        ans += 1
    ans += i//K
print(ans)