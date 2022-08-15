import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [i+1 for i in range(n)]
arr = []
def permutation_with_repitition(x):
    if x == m:
        print(*arr)
        return
    for i in range(n):
        arr.append(num_list[i])
        permutation_with_repitition(x+1)
        arr.pop()
permutation_with_repitition(0)