import sys
import heapq
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    candidate = []
    for _ in range(n):
        candidate.append(tuple(map(int, sys.stdin.readline().split())))
    candidate.sort(key=lambda x: x[0])
    standard = []
    now = candidate[0]
    heapq.heappush(standard, now)
    for i in range(1, n):
        if candidate[i][1] < now[1]:
            heapq.heappush(standard, candidate[i])
            now = candidate[i]
    print(len(standard))