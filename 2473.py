import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
diff = sys.maxsize
l, m, r = 0, 0, 0
for i in range(n-2):
    start = i + 1
    end = n - 1
    while start < end:
        temp = arr[start] + arr[i] + arr[end]
        if diff > abs(temp):
            l = i
            m = start
            r = end
            diff = abs(temp)
        if temp > 0: end -= 1
        else: start += 1
print(arr[l], arr[m], arr[r])