import sys
Mod = 1000000007
n = int(sys.stdin.readline())
arr = [[1, 1], [1, 0]]


def fib(A, B):
    new = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                new[i][j] += A[i][k] % Mod * B[k][j] % Mod
            new[i][j] %= Mod
    return new


def involution(A, B):
    if B==1:
        return A
    m=involution(A, B//2)
    if B%2:
        return fib(fib(m, m), A)
    else:
        return fib(m, m)


print(involution(arr, n)[0][1])