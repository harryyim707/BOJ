import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
arr.sort()
for i in range(n):
    print("{} {}".format(arr[i][1], arr[i][0]))