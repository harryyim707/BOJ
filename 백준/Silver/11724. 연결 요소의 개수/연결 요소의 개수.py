import sys
sys.setrecursionlimit(10**7)
n, m = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        dfs(i)
print(cnt)