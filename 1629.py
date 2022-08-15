import sys
a, b, c = map(int, sys.stdin.readline().split())


def sol(x):
    global a, c
    if x == 1:
        return a%c
    temp = sol(x//2)
    if x%2 == 0:
        return temp*temp%c
    else:
        return temp*temp*a%c


print(sol(b))