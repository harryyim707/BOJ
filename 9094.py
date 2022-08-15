import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    cnt = 0
    m, n = map(int, input().split())
    for a in range(1, n-1):
        for b in range(a+1, n):
            res = (a**2+b**2+m)/(a*b)
            if res.is_integer():
                cnt += 1
    print(cnt)