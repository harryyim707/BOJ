import sys
A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())
dp = [0] * 1000
for i in range(len(A)):
    MAX = 0
    for j in range(len(B)):
        if MAX < dp[j]:
            MAX = dp[j]
        elif A[i] == B[j]:
            dp[j] = MAX+1
print(max(dp))