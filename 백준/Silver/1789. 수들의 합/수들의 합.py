import sys
s = int(sys.stdin.readline().rstrip())
cnt = 0
total = 0
while True:
    cnt += 1
    total += cnt
    if total > s:
        break
print(cnt - 1)