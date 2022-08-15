n = int(input())
k = int(input())
l, r = 1, n*n
ans = 0
while l <= r:
    m = (l+r)//2
    cnt = 0
    if m < k:
        l = m+1
    else:
        r = m-1
        break
print(ans)
