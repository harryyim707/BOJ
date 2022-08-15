import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))
k = num[0]
num_max = -1000000001
num_min = 1000000001


def dfs(cnt, k, plus, minus, multiply, divide):
    global num_min
    global num_max
    if cnt == n:
        num_min = min(k, num_min)
        num_max = max(k, num_max)
    if plus:
        dfs(cnt + 1, k + num[cnt], plus - 1, minus, multiply, divide)
    if minus:
        dfs(cnt + 1, k - num[cnt], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(cnt + 1, k * num[cnt], plus, minus, multiply - 1, divide)
    if divide:
        dfs(cnt + 1, k // num[cnt] if k >= 0 else -(-k//num[cnt]), plus, minus, multiply, divide - 1)


dfs(1, k, oper[0], oper[1], oper[2], oper[3])
print(num_max)
print(num_min)