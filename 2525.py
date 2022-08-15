import sys
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
hour  = A
minute = B+C
if minute < 60:
    pass
else:
    hour = (hour + minute // 60) % 24
    minute %= 60
print(hour, minute)