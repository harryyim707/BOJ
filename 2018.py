n = int(input())
s, e = 0, 1
cnt = 0
t = 1
while s <= n and s <= e:
    if t < n:
        e += 1
        t += e
    elif t == n:
        cnt += 1
        e += 1
        t -= s
        t += e
        s += 1
    else:
        t -= s
        s += 1
print(cnt)