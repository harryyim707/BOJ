import sys
from collections import deque
n = int(sys.stdin.readline())
deq = deque()
for _ in range(n):
    oper = list(sys.stdin.readline().rstrip().split())
    if oper[0] == 'push_front':
        deq.appendleft(int(oper[1]))
    if oper[0] == 'push_back':
        deq.append(int(oper[1]))
    if oper[0] == 'pop_front':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
    if oper[0] == 'pop_back':
        if not deq:
            print(-1)
        else:
            print(deq.pop())
    if oper[0] == 'size':
        print(len(deq))
    if oper[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    if oper[0] == 'front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    if oper[0] == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])