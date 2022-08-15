import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]


def sol(n, x, y):
    k = n // 2
    if k == 0: return arr[x][y]
    a1 = sol(k, x, y)
    a2 = sol(k, x, y+k)
    a3 = sol(k, x+k, y)
    a4 = sol(k, x+k, y+k)
    if ((a1 == 0 or a1 == 1) and a1 == a2 == a3 == a4): return a1
    s = f"({a1}{a2}{a3}{a4})"
    return s


print(sol(n, 0, 0))
