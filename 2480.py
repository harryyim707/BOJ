import sys
a, b, c = map(int, sys.stdin.readline().split())
dice = [a, b, c]
dice.sort()
if a == b == c:
    price = 10000+1000*dice[0]
elif a != b and b != c and c != a:
    price = dice[2] * 100
else:
    price = dice[1]*100 + 1000
print(price)
