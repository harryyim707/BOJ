from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]


def bfs(x, y, wall, graph, visited):
    q = deque()
    q.append((x, y, wall))
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    visited[y][x][wall] = 1
    while q:
        x, y, wall = q.popleft()
        if x == m-1 and y == n-1:
            return visited[y][x][wall]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 0 and visited[ny][nx][wall] == 0:
                q.append((nx, ny, wall))
                visited[ny][nx][wall] = visited[y][x][wall] + 1
            if graph[ny][nx] == 1 and wall == 1:
                q.append((nx, ny, wall-1))
                visited[ny][nx][wall - 1] = visited[y][x][wall] + 1
    return -1


print(bfs(0, 0, 1, graph, visited))