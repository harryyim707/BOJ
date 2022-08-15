import sys


def check(x):
    for i in range(x):
        if arr[i] == arr[x] or abs(arr[i] - arr[x]) == x-i:
            return False
    return True


def dfs(x):
    global count

    if x == n:
        count += 1
    else:
        for i in range(n):
            arr[x] = i
            if check(x):
                dfs(x + 1)

n = int(sys.stdin.readline())
arr = [0] * n
count = 0
dfs(0)
print(count)