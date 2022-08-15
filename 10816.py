from bisect import bisect_left, bisect_right
n = int(input())
arr = sorted(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))
res = [0]*m
for i in range(m):
    res[i] = bisect_right(arr, num[i]) - bisect_left(arr, num[i])
print(*res)