import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
q = deque(range(1, n+1))
result = []
temp = k-1
while True:
    if len(q) == 0:
        break
    q.rotate(-k)
    p = q.pop()
    result.append(str(p))
print(f"<{', '.join(result)}>")