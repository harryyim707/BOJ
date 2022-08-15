import sys
sudoku = [list(map(int, sys.stdin.readline().split()))for _ in range(9)]
zeroes = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def isPromising(i, j):
    promising = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for k in range(9):
        if sudoku[i][k] in promising:           #가로 check
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:           #세로 check
            promising.remove(sudoku[k][j])
    #박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])
    return promising


flag = False


def dfs(x):
    global flag
    if flag:
        return
    if x == len(zeroes):
        for row in sudoku:
            print(*row)
        flag = True
        return
    else:
        (i, j) = zeroes[x]
        promising = isPromising(i, j)

        for num in promising:
            sudoku[i][j] = num
            dfs(x+1)
            sudoku[i][j] = 0


dfs(0)