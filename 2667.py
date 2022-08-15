import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited):
    q = deque()
    q.append([x, y])
    cnt = 0
    while q:
        x, y = q.popleft()
        if visited[x][y] == False:
            visited[x][y] = True
            cnt += 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == False and graph[nx][ny] == 1:
                    q.append([nx, ny])
    return cnt


visited = [[False for _ in range(N)] for _ in range(N)]
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and graph[i][j] == 1:
            cnt += 1
            result.append(bfs(i, j, visited))
result.sort()
print(cnt)
for i in result:
    print(i)
