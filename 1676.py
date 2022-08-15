import sys
n = int(sys.stdin.readline())
cnt = 0
temp = 1
for i in range(1, n+1):
    temp *= i
while True:
    if temp % 10 == 0:
        cnt += 1
    else:
        break
    temp //= 10

print(cnt)