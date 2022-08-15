import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().split()))
arr.sort(key=lambda a:int(a[0]))

for i in arr:
    print("{} {}".format(i[0], i[1]))