import sys
n = int(sys.stdin.readline())
arr = [i for i in range(1, n+1)]
cnt = 0
for i in range(n):
    t = arr[i]
    s = 0
    while t > 0:
        s += t % 10
        t //= 10
    if arr[i] % s == 0: cnt += 1
print(cnt)