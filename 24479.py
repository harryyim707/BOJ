import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, r = map(int, input().split())
g = [[]for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 1


def dfs (graph, v, visited):
    global cnt
    visited[v] = cnt
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)


for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
for i in range(n+1):
    g[i].sort()
dfs(g, r, visited)
for i in range(n+1):
    if i:
        print(visited[i])