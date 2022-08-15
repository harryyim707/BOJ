import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
sum = 0
for i in range(n):
    sum += num[i]
    num[i] = sum
sum = 0
for i in num:
    sum += i
print(sum)