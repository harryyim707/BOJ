import sys
n = int(sys.stdin.readline())
num = [[0 for _ in range(10)]for _ in range(101)]

for i in range(1, 10):
    num[1][i] = 1;

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            num[i][j] = num[i-1][j+1]
        elif j == 9:
            num[i][j] = num[i-1][j-1]
        else:
            num[i][j] = (num[i-1][j-1]+num[i-1][j+1])%1000000000

sum = 0
for i in range(10):
    sum += (num[n][i] % 1000000000)

print(sum%1000000000)