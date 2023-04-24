import sys
from heapq import heappop, heappush
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    heappush(arr, int(sys.stdin.readline()))
if len(arr) == 1:
    print(0)
else:
    answer = 0
    while len(arr) > 1:
        t1 = heappop(arr)
        t2 = heappop(arr)
        answer += t1+t2
        heappush(arr, t1+t2)
    print(answer)