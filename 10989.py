import sys
n = int(sys.stdin.readline())
number = [0] * 10001

for i in range(n):
    number[int(sys.stdin.readline().strip())] += 1

for i in range(1, 10001):
    for _ in range(number[i]):
        print(i)