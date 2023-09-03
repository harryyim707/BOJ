r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(input()))
visited = [[False for _ in range(c)] for _ in range(r)]
result = 0


def dfs(x, y):
    if x == c-1:
        return True
    dy = [-1, 0, 1]
    visited[y][x] = True
    for i in range(3):
        nx, ny = x + 1, y + dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            if arr[ny][nx] != 'x' and not visited[ny][nx]:
                visited[ny][nx] = True
                if dfs(nx, ny):
                    return True
    return False


for i in range(r):
    if dfs(0, i): result += 1
print(result)