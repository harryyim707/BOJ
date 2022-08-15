n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
num = list(map(int, input().split()))
for i in num:
    left, right = 0, n-1
    while True:
        if left > right:
            print(0)
            break
        mid = (left+right)//2
        if arr[mid] == i:
            print(1)
            break
        elif arr[mid]>i: right = mid-1
        else: left = mid + 1