n, k = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
ans = -1

def sel(arr):
    global cnt, ans
    for i in range(n-1, 0, -1):
        max_item, idx = arr[0], 0
        for j in range(1, i+1):
            if arr[j] > max_item:
                max_item, idx = arr[j], j
        if arr[i] != arr[idx]:
            arr[i], arr[idx] = arr[idx], arr[i]
            cnt += 1
        if cnt == k:
            ans = f'{arr[idx]} {arr[i]}'
    return ans

print(sel(num))