import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
m, n = list(map(int, sys.stdin.readline().split()))
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
q = deque()
cnt = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            q.append([x, y])


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])


bfs()
for row in graph:
    for t in row:
        if t == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(row))
print(cnt-1)
