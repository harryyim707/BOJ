import sys
n = int(sys.stdin.readline())
arr = []
stack = []
prt = []
num = [i+1 for i in range(n)]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

i = 0
cnt = 0
while True:
    if len(stack) == 0:
        stack.append(num[i])
        prt.append("+")
        i += 1
    else:
        if stack[len(stack)-1] == arr[cnt]:
            stack.pop()
            prt.append("-")
            cnt += 1
        else:
            if i == n:
                print("NO")
                break
            stack.append(num[i])
            prt.append("+")
            i += 1
    if cnt == n:
        for i in prt:
            print(i)
        break