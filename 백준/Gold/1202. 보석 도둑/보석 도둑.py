import heapq
n, k = map(int, input().split())
jewerly = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewerly, (m, v))
bag = []
for _ in range(k):
    bag.append(int(input()))
bag.sort()
tmp = []
ans = 0
for c in bag:
    while jewerly and c >= jewerly[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewerly)[1])
    if tmp:
        ans -= heapq.heappop(tmp)
    elif not jewerly:
        break
print(ans)