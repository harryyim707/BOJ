import sys, heapq
n = int(sys.stdin.readline())
num = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if not x:
        if num:
            print(heapq.heappop(num)[1])
        else:
            print(0)
    else:
        heapq.heappush(num, (abs(x), x))