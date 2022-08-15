import bisect
k, n = map(int, input().split())
arr = []
res = 0
for _ in range(k):
    arr.append(int(input()))
l, r = 1, max(arr)
while l <= r:
    m = (l+r)//2
    cnt = 0
    for i in arr:
        cnt += i//m
    if cnt < n:
        r = m - 1
    else:
        l = m + 1
        if res < m:
            res = m
        else:
            continue
print(res)