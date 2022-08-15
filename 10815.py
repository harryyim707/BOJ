import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
m = int(sys.stdin.readline())
sample = list(map(int, sys.stdin.readline().split()))


def BS(arr, start, end, target):
    if start > end:
        return 0
    mid = (start + end)//2
    if arr[mid] == target:
        return 1
    elif arr[mid]>target:
        return BS(arr, start, mid-1, target)
    else:
        return BS(arr, mid+1, end, target)

for i in range(m):
    print(BS(num, 0, n-1, sample[i]), end=' ')