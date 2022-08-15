import sys
from collections import deque
t = int(sys.stdin.readline())
errFlag = False
for _ in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()[1:-2].split(",")

    if arr[0] != "":
        arr = deque(arr)
    else:
        arr = deque()
    direction_flag = True
    for i in p:
        if i == "R":
            if direction_flag == True:
                direction_flag = False
            elif direction_flag == False:
                direction_flag = True
        elif i == "D":
            if len(arr) == 0:
                print("error")
                errFlag = True
                break
            if direction_flag == True:
                arr.popleft()
            elif direction_flag == False:
                arr.pop()

    if p.count("R") % 2 != 0:
        arr.reverse()
    if errFlag == False:
        print("[", end="")
        for j in range(len(arr)):
            print(arr[j], end="")
            if j != len(arr) - 1:
                print(",", end="")
        print("]")
    errFlag = False