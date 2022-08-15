import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    n, x = map(int, sys.stdin.readline().split())
    q = deque(map(int, sys.stdin.readline().split()))
    idx_que = deque(list(range(n)))
    cnt = 0
    while q:
        if q[0] == max(q):
            cnt += 1
            q.popleft()
            if idx_que.popleft() == x:
                print(cnt)
        else:
            q.append(q.popleft())
            idx_que.append(idx_que.popleft())