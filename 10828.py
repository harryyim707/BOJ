import sys
n = int(sys.stdin.readline())
q = []
for _ in range(n):
    order = list(sys.stdin.readline().rstrip().split())
    if order[0] == 'push':
        q.append(int(order[1]))
    elif order[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.pop(-1))
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if not q:
            print(-1)
        else:
            print(q[-1])