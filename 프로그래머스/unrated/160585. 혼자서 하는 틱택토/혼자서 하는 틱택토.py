def check(x, board):
    #행 확인
    for i in range(3):
        if all(row == x for row in board[i]):
            return True
    #열 확인
    for j in range(3):
        if all(board[i][j] == x for i in range(3)):
            return True
    #대각선 확인
    if all(board[i][i] == x for i in range(3)):
        return True
    if all(board[i][2-i] == x for i in range(3)):
        return True
    return False

def solution(board):
    answer = 1
    cnt_O = sum(row.count("O") for row in board)
    cnt_X = sum(row.count("X") for row in board)
    
    if cnt_X>cnt_O or abs(cnt_X-cnt_O) > 1:
        answer = 0
    elif (check('O', board) and cnt_X != cnt_O-1) or (check('X', board) and cnt_X != cnt_O):
        answer = 0
    
    return answer