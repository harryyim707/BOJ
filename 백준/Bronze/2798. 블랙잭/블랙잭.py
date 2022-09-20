import sys
def find(a, b):
    a = list(a)
    answer = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                sum = a[i]+a[j]+a[k]
                if sum <= b:
                    answer = max(answer, sum)
    print(answer)

n, m = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
find(arr, m)
