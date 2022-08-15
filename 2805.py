N, M = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, max(arr)
res = 0
while l <= r:
    cnt = 0
    m = (l+r)//2
    for i in arr:
        if i > m:
            cnt += i-m
        if cnt >= M:
            break
    if cnt >= M:
        res = max(res, m)
        l = m+1
    else:
        r = m-1
print(res)
