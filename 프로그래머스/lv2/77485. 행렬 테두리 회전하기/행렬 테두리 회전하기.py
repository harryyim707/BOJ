from collections import deque
def solution(rows, columns, queries):
    answer = []
    arr = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(rows):
        tmp = []
        for j in range(columns * i + 1, columns * (i + 1) + 1):
            tmp.append(j)
        arr.append(tmp)
    for query in queries:
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        que = deque()
        i = 0
        x, y = x1, y1+1
        que.append(arr[x][y])
        res = 10000
        while True:
            if x == x1 and y == y1:
                arr[x][y+1] = que.popleft()
                res = min(res, arr[x][y+1])
                answer.append(res)
                break
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx == x1 and ny == y2+1) or (nx == x2+1 and ny == y2) or (nx == x2 and ny == y1-1) or (nx == x1-1 and ny == y1):
                i += 1
                nx = x + dx[i]
                ny = y + dy[i]
            que.append(arr[nx][ny])
            arr[nx][ny] = que.popleft()
            res = min(res, arr[nx][ny])
            x, y = nx, ny
    return answer