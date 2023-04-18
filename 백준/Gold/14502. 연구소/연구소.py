import sys
import copy
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0


def bfs():
    q = deque()
    t_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if t_graph[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if t_graph[nx][ny] == 0:
                    t_graph[nx][ny] = 2
                    q.append((nx, ny))
    global answer
    cnt = 0
    for i in range(n):
        for j in range(m):
            if t_graph[i][j] == 0:
                cnt += 1
    answer = max(answer, cnt)


def makewall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makewall(cnt+1)
                graph[i][j] = 0


makewall(0)
print(answer)