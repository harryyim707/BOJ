import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num_list = [1+i for i in range(n)]
visited = [False]*n
arr =[]
def permutation(x):
    if x == m:
        print(*arr)
        return
    else:
        for i in range(n):
            if visited[i]:
                continue
            arr.append(num_list[i])
            visited[i] = True
            permutation(x+1)
            arr.pop()
            visited[i] = False
permutation(0)