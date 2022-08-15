n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())
l, r = 0, n-1
cnt = 0
while l < r < n:
    if arr[l] + arr[r] == x:
        cnt += 1
        l += 1
        r -= 1
    else:
        if arr[l]+arr[r] < x:
            l += 1
        else:
            r -= 1
print(cnt) 