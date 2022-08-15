import sys
n, k = map(int, sys.stdin.readline().split())


def factorial(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)


result = factorial(n) // (factorial(k) * factorial(n-k))
print(result)