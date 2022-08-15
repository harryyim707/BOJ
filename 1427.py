import sys
arr = list(sys.stdin.readline().rstrip())
for i in range(len(arr)):
    arr[i] = int(arr[i])
arr = sorted(arr, reverse=True)
for i in arr:
    print(i, end='')
