import sys
t = int(sys.stdin.readline())
for _ in range(t):
  n = int(sys.stdin.readline())
  L = list(map(int, sys.stdin.readline().split()))
  L.sort()
  Max = L[1]-L[0]
  for i in range(n-2):
    Max = max(Max, L[i+2]-L[i])
  Max = max(Max, L[n-1]-L[n-2])
  print(Max)