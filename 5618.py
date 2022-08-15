n = int(input())
num = list(map(int, input().split()))


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)


g = gcd(num[0], gcd(num[1], num[-1]))
for i in range(1, (g//2)+1):
    if g % i == 0:
        print(i)
print(g)