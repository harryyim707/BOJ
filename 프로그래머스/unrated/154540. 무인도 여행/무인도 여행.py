from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, r, c, visited, maps):
    que = deque([(x, y)])
    visited[x][y] = True
    cost = int(maps[x][y])
    while que:
        cx, cy = que.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != 'X':
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    cost += int(maps[nx][ny])
                    que.append((nx, ny))
    return visited, cost


def solution(maps):
    answer = []
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited, ans = bfs(i, j, len(maps), len(maps[0]), visited, maps)
                answer.append(ans)
    return sorted(answer) if answer else [-1]