import sys
n, m = map(int, sys.stdin.readline().split())


def gcd(a, b):
    if a%b == 0:
        return b
    else:
        gcd(b, a % b)


print(gcd(n, m))
print(n*m//gcd(a,b))