from collections import deque
import sys


def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    q = deque()
    q.append(v)
    visited2[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visited2[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited2[i] = 1


n, m, v = list(map(int, sys.stdin.readline().split()))
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = list(map(int, sys.stdin.readline().split()))
    graph[x][y] = graph[y][x] = 1
visited = [0 for _ in range(n + 1)]
visited2 = [0 for _ in range(n + 1)]
dfs(v)
print()
bfs(v)
