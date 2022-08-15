import sys
k = int(sys.stdin.readline())
q = []
for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        q.pop(-1)
    else:
        q.append(n)
print(sum(q))