import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [i+1 for i in range(n)]
arr = []
def combination_with_repitition(x, index):
    if x == m:
        print(*arr)
        return
    for i in range(index, n):
        arr.append(num_list[i])
        combination_with_repitition(x+1, i)
        arr.pop()
combination_with_repitition(0, 0)