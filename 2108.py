import sys
from collections import Counter
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))


def mode(arr):
    mode_dict = Counter(arr)
    modes = mode_dict.most_common()
    if len(arr) > 1:
        if modes[0][1] == modes[1][1]:
            mode_num = modes[1][0]
        else:
            mode_num = modes[0][0]
    else:
        mode_num = modes[0][0]
    return mode_num


def median(arr):
    arr.sort()
    mid = arr[len(arr)//2]
    return mid


def mean(arr):
    return round(sum(arr)/len(arr))


def scope(arr):
    return max(arr) - min(arr)

print(mean(arr))
print(median(arr))
print(mode(arr))
print(scope(arr))