n = int(input())
num = list(map(int, input().split()))
k = int(input())
arr = [0 for i in range(n+1)]
arr[0] = 0
for i in range(1, n+1):
    arr[i] = arr[i-1] + num[i-1] #누적합을 전부 구해 준다
start, end, ans = 0, 1, 0
while True:
    if end > n or start > n: #만약 포인터들이 n을 넘어가면 index error가 발생하므로 탈출 조건
        break
    if arr[end] - arr[start] <= k: #누적합에서 두 개의 index끼리의 차를 구한다면 그 구간 사이의 합을 구할 수 있음
        end += 1
    else:
        ans += (n - end + 1) # n + 1으로부터 end의 위치를 빼주면 그 사이의 값들은 전부 포함된다.
        start += 1 #포인터의 값을 다음 포인터로 옮겨준다
        end = start + 1
print(ans)