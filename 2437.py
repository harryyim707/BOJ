import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
s = arr[0]
if s != 1 : s = 0
else:
    for i in range(1, n):
        if arr[i] <= s + 1: s += arr[i]
        else: break
print(s + 1)