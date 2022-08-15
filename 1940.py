n = int(input())
m = int(input())
arr = sorted(map(int, input().split()))
cnt = 0
s, e = 0, n-1
while s < e:
    t = arr[s] + arr[e]
    if t == m:
        cnt += 1
        s += 1
        e -= 1
    elif t > m:
        e -= 1
    else:
        s += 1
print(cnt)