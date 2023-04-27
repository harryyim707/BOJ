import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
max_h = 0
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    max_h = max(max_h, max(tmp))
    graph.append(tmp)


def bfs(x, y, h, visited):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited[y][x] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] > h and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((nx, ny))


result = 0
for i in range(max_h):
    cnt = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if graph[y][x] > i and visited[y][x] == 0:
                bfs(x, y, i, visited)
                cnt += 1
    result = max(result, cnt)
print(result)
