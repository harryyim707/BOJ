def solution(park, routes):
    op = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}
    n, m = len(park), len(park[0])
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                x, y = i, j
                break
    for cmd in routes:
        oper, cnt = cmd.split()
        flag = True
        sx, sy = x, y
        for i in range(int(cnt)):
            dx, dy = op[oper]
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < m and park[nx][ny] != "X":
                x, y = nx, ny
            else:
                x, y = sx, sy
                break
    return x, y