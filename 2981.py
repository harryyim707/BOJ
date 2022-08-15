import sys


def GCD(x, y):
    return GCD(y, x % y) if y else x


n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
m = num[1] - num[0]
for i in range(2, n):
    m = GCD(m, num[i]- num[i-1])
for i in range(2, m//2 + 1):
    if m % i == 0:
        print(i, end=" ")
print(m)