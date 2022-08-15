import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    oper = sys.stdin.readline().rstrip().split()
    if oper[0] == 'push':
        q.append(int(oper[1]))
    if oper[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    if oper[0] == 'size':
        print(len(q))
    if oper[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    if oper[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    if oper[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
