import sys
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
arr = list(sorted(set(x)))
dic = {value: index for index, value in enumerate(arr)}

for i in x:
    print(dic[i], end=' ')