import sys
from math import gcd
a,b=map(int, sys.stdin.readline().split())
ans = a
for i in range(a+1, b+1):
    for j in range(1, i):
        if a > i - i // gcd(i,j):
            ans += 1
print(ans)