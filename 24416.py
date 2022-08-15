#pypy3
n = int(input())


def fib1(x):
    if x == 1 or x == 2:
        return 1
    return fib1(x-1)+fib1(x-2)


def fib2(x):
    cnt = 0
    fib = [0]*(n+1)
    fib[1] = fib[2] = 1
    for i in range(3, x+1):
        cnt += 1
        fib[i] = fib[i-1] + fib[i-2]
    return cnt


print(fib1(n), fib2(n))