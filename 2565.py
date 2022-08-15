import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a, b])
arr = sorted(arr, key = lambda x:x[0])
dp = [[]for _ in range(n)]
for i in range(n):
    if i == 0:
        dp[i].append(arr[i][1])
    else:
        for j in range(i):
            if dp[j][-1] < arr[i][1]:
                if len(dp[i]) - 1 < len(dp[j]):
                    dp[i] = dp[j] + [arr[i][1]]
            if not dp[i]:
                dp[i].append(arr[i][1])
maximum = 0
for i in range(n):
    maximum = max(maximum, len(dp[i]))
print(n-maximum)