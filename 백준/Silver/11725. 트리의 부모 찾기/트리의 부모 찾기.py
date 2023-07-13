from collections import deque
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

queue = deque()
queue.append(1)

arr = [0] * (n+1)
while queue:
    cur = queue.popleft()
    for next in tree[cur]:
        if arr[next] == 0:
            arr[next] = cur
            queue.append(next)
res = arr[2:]
for x in res:
    print(x)