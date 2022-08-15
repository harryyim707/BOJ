import sys
N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
D = []
ans = C
budget = A
for _ in range(N):
    k = int(sys.stdin.readline())
    D.append(k)
D.sort()
for i in range(N-1, -1, -1):
    if ((ans + D[i]) / (budget + B)) > (ans / budget):
        ans += D[i]
        budget += B
print(ans // budget)