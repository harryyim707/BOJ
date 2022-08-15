import sys
t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().strip()
    stack = 0
    for i in s:
        if i == "(":
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print("YES")
    else:
        print("NO")