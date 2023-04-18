import sys
from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[y][x] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                q.append((nx, ny))
                graph[ny][nx] = 0


t = int(sys.stdin.readline())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for _ in range(t):
    m, n, k = list(map(int, sys.stdin.readline().split()))
    graph = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = list(map(int, sys.stdin.readline().split()))
        graph[y][x] = 1
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                bfs(x, y)
                cnt += 1
    print(cnt)
