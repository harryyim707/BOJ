import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(reverse=True)


def solution(arr, m):
    if m == 1:
        return "YES"
    for i in range(1, len(arr)):
        for j in range(m):
            if arr[i-1][j] == 0 and arr[i][j] == 1:
                return "NO"

    return "YES"


print(solution(arr,m))
