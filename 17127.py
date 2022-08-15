n = int(input())
arr = list(map(int, input().split()))


def func(l):
    x = 1
    for i in l:
        x *= i
    return x


ans = 0
for i in range(4):
    t = func(arr[i:i+n-3])+sum(arr) - sum(arr[i:i+n-3])
    if t > ans:
        ans = t
print(ans)