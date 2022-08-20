import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sum_arr = [[0 for _ in range(n+1)]for _ in range(n+1)] 
for i in range(n):
    for j in range(n):
        sum_arr[i+1][j+1] = sum_arr[i+1][j] + sum_arr[i][j+1] + arr[i][j] - sum_arr[i][j]
for _ in range(m):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    print(sum_arr[x_2][y_2]-sum_arr[x_2][y_1-1] - sum_arr[x_1-1][y_2] + sum_arr[x_1-1][y_1-1])