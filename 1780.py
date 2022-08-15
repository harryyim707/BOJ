import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
a, b, c = 0, 0, 0


def sol(arr, k):
    global a, b, c
    default = arr[0][0]
    flag = 1
    for i in arr:
        for j in i:
            if default != j:
                flag = 0
                break
    if flag:
        if default == -1:
            a += 1
        elif default == 0:
            b += 1
        elif default == 1:
            c += 1
        return
    a1, a2, a3, a4, a5, a6, a7, a8, a9 = [], [], [], [], [], [], [], [], []
    k //= 3
    for i in range(k):
        a1.append(arr[i][:k])
        a4.append(arr[i+k][:k])
        a7.append(arr[i+2*k][:k])
        a2.append(arr[i][k:2*k])
        a5.append(arr[i+k][k:2*k])
        a8.append(arr[i+2*k][k:2*k])
        a3.append(arr[i][2*k:])
        a6.append(arr[i+k][2*k:])
        a9.append(arr[i+2*k][2*k:])
    return sol(a1, k), sol(a2, k), sol(a3, k), sol(a4, k), sol(a5, k), sol(a6, k), sol(a7, k), sol(a8, k), sol(a9, k)


sol(arr, n)
print(a)
print(b)
print(c)