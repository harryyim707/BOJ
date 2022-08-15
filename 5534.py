import sys
N = int(sys.stdin.readline())
name = sys.stdin.readline().rstrip()
n = len(name)
cnt = 0
for _ in range(N):
    board = list(sys.stdin.readline().rstrip())
    length = len(board)
    for i in range(length):
        for j in range(1, length):
            if i + j * (n-1) >= length: continue
            tab = ''.join(board[i+j*k] for k in range(n))
            if tab == name: cnt += 1; break
        else: continue
        break
print(cnt)