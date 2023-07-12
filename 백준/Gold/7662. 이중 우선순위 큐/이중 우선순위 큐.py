import heapq
t = int(input())
for _ in range(t):
    k = int(input())
    visited = [False] * k
    q_min, q_max = [], []
    for i in range(k):
        operation, n = input().split()
        n = int(n)
        if operation == 'I':
            heapq.heappush(q_min, (n, i))
            heapq.heappush(q_max, (-n, i))
            visited[i] = True
        elif operation == 'D':
            if n == -1:
                while q_min and not visited[q_min[0][1]]:
                    heapq.heappop(q_min)
                if q_min:
                    visited[q_min[0][1]] = False
                    heapq.heappop(q_min)
            elif n == 1:
                while q_max and not visited[q_max[0][1]]:
                    heapq.heappop(q_max)
                if q_max:
                    visited[q_max[0][1]] = False
                    heapq.heappop(q_max)
    while q_min and not visited[q_min[0][1]]:
        heapq.heappop(q_min)
    while q_max and not visited[q_max[0][1]]:
        heapq.heappop(q_max)
    if q_min and q_max:
        print(-q_max[0][0], q_min[0][0])
    else:
        print('EMPTY')