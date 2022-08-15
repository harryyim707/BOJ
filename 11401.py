import sys
n, k = map(int, sys.stdin.readline().split())
M = 1000000007


def facmod(n):
    global M
    result = 1
    for i in range(1, n+1):
        result = (result*i) % M
    return result


def expmod(n, e):
    global M
    if e == 1: return n
    if e % 2 == 1 : return (expmod(n, e-1)*n) % M

    half = expmod(n, e//2)
    return (half * half) % M

def solve(n, k):
    global M
    nmod = facmod(n)
    kmod = facmod(k)
    nkmod = facmod(n-k)

    emod = expmod((kmod*nkmod)%M, M-2)
    return (nmod*emod)%M


print(solve(n, k))