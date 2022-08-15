import sys
n, m = map(int, sys.stdin.readline().split())


def cal(x, y):
    cnt = 0
    while x:
        x //= y
        cnt += x
    return cnt


a5 = cal(n, 5) - cal(m, 5) - cal(n-m, 5)
a2 = cal(n, 2) - cal(m, 2) - cal(n-m, 2)
print(min(a5, a2))