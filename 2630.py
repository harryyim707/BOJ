import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
blue = 0
white = 0
print(arr)

def sol(arr, k):
    global blue, white
    if check(arr) == k*k:
        blue += 1
        return
    elif check(arr) == 0:
        white += 1
        return
    one, two, three, four = [], [], [], []
    k //= 2
    for i in range(k):
        one.append(arr[i][:k])
        two.append(arr[i+k][:k])
        three.append(arr[i][k:])
        four.append(arr[i+k][k:])
    return sol(one, k), sol(two, k), sol(three, k), sol(four, k)


def check(arr):
    result = 0
    for i in arr:
        result += (sum(i))
    return result


sol(arr, n)
print(white)
print(blue)