import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0]
cnt = [0] * m
for i in range(n):
    arr[i] += arr[i-1]
    cnt[arr[i]%m] += 1
ans = cnt[0]
for v in cnt:
    ans += v * (v-1) // 2
print(ans)