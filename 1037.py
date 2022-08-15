import sys
number = int(sys.stdin.readline())
mod = list(map(int, sys.stdin.readline().split()))
print(min(mod)*max(mod))