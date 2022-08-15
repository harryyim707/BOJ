import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
start = 0
end = n-1
diff = sys.maxsize
l, r = 0, 0
while start < end:
    temp = arr[start] + arr[end]
    if diff > abs(temp):
        diff = abs(temp)
        l = start; r = end
    if temp > 0:
        end -= 1
    else:
        start += 1
print(arr[l], arr[r])