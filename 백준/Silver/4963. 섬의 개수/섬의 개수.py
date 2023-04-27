import sys
from collections import deque


def bfs(x, y, graph, visited):
    dx = [0, 0, -1, 1, 1, 1, -1, -1]
    dy = [-1, 1, 0, 0, -1, 1, 1, -1]
    q = deque()
    visited[y][x] = 1
    q.append((x, y))
    w, h = len(graph[0]), len(graph)
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    q.append((nx, ny))
                    visited[ny][nx] = 1


while True:
    w, h = map(int, sys.stdin.readline().split())
    if (w, h) == (0, 0):
        break
    graph = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    cnt = 0
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(j, i, graph, visited)
                cnt += 1
    print(cnt)