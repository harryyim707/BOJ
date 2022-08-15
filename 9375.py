import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        name, kind = sys.stdin.readline().split()
        dic[kind] = dic.get(kind, 0) + 1
    ans = 1
    for k, c in dic.items():
        ans *= (c+1)
    ans -= 1
    print(ans)