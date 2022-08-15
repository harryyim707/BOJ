import sys, heapq
n = int(sys.stdin.readline())
l_heap = []
r_heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap, (-num, num))
    else:
        heapq.heappush(r_heap, (num, num))
    if r_heap and l_heap[0][1] > r_heap[0][1]:
        l = heapq.heappop(l_heap)[1]
        r = heapq.heappop(r_heap)[1]
        heapq.heappush(r_heap, (l, l))
        heapq.heappush(l_heap, (-r, r))

    print(l_heap[0][1])