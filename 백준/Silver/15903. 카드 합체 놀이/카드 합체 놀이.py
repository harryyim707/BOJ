import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))
arr = []
for i in range(n):
    heapq.heappush(arr, a[i])
for _ in range(m):
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    z = x + y
    heapq.heappush(arr, z)
    heapq.heappush(arr, z)
print(sum(arr))