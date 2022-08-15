n, c = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
l, r = 1, arr[-1]-arr[0]
ans = 0
while l <= r:
    m = (l+r)//2
    cnt = 1
    cur = arr[0]
    for i in range(1, n):
        if arr[i]-cur >= m:
            cnt += 1
            cur = arr[i]
    if cnt >= c:
        l = m + 1
        ans = m
    else:
        r = m - 1
print(ans)