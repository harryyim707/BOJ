import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
q = deque(range(1, n+1))

total = 0

for idx in range(len(num)):
    if num[idx] == q[0]:
        q.popleft()
        continue
    q_idx = q.index(num[idx])

    if q_idx > len(q) // 2:
        q.rotate(len(q)-q_idx)
        total += (len(q)-q_idx)

    elif q_idx <= len(q) // 2:
        q.rotate(-q_idx)
        total += q_idx
    q.popleft()
print(total)