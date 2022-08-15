import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [i+1 for i in range(n)]
visited = [False]*n
arr = []
def combination(x, index):
    if x == m:
        print(*arr)
    for i in range(index, n):
        if visited[i]:
            continue
        arr.append(num_list[i])
        visited[i] = True
        combination(x+1, i+1)
        arr.pop()
        visited[i] = False

combination(0, 0)