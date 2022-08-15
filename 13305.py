import sys
n = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
standard = price[0]
result = 0
prev = 0
for i in range(n-1):
    if price[i] <= standard:
        result += length[i] * price[i]
        standard = price[i]
        prev = price[i]
    else:
        result += prev * length[i]
print(result)