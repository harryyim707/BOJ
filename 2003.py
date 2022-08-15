n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0]
l, r = -1, -1
s, cnt = 0, 0
while l <= r and r < n:
    if s > m:
        l += 1
        s -= arr[l]
    elif s < m:
        r += 1
        s += arr[r]
    elif s == m:
        cnt += 1
        r += 1
        s += arr[r]
print(cnt)