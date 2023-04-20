import sys
from collections import deque

dx = [0, 0, -1, 1, 0, 0]  # 상, 하, 좌, 우, 앞 뒤
dy = [0, 0, 0, 0, -1, 1]  # 0 <= x < m, 0 <= y < n, 0 <= z < h
dz = [1, -1, 0, 0, 0, 0]
m, n, h = map(int, sys.stdin.readline().split())
graph = []
for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
    graph.append(tmp)

q = deque()
cnt = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                q.append([x, y, z])


def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                q.append([nx, ny, nz])


bfs()
for story in graph:
    for row in story:
        for t in row:
            if t == 0:
                print(-1)
                exit(0)
        cnt = max(cnt, max(row))
print(cnt - 1)