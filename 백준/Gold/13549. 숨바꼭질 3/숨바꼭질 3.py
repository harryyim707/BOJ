import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
MAX = 10 ** 5
visited = [-1] * (MAX+1)
visited[n] = 0
q = deque()
q.append(n)
while q:
    s = q.popleft()
    if s == k:
        print(visited[s])
        break
    if 0 <= s-1 <= MAX and visited[s-1] == -1:
        visited[s-1] = visited[s]+1
        q.append(s-1)
    if 0 <= s*2 <= MAX and visited[s*2] == -1:
        visited[s*2] = visited[s]
        q.appendleft(s*2)
    if 0 <= s+1 <= MAX and visited[s+1] == -1:
        visited[s+1] = visited[s]+1
        q.append(s+1)