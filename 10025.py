N, K = map(int, input().split())
arr = [0 for _ in range(1000001)]
left, right = 10000, 0
for _ in range(N):
    g, x = map(int, input().split())
    arr[x] = g
    left = min(left, x)
    right = max(right, x)

end = left
now, ans = 0, 0
for i in range(left, right+1):
    while end < right + 1 and end - i <= K * 2:
        if not arr[end]:
            end += 1
            continue
        now += arr[end]
        end += 1
    ans = max(ans, now)
    now -= arr[i]
    if end >= right: break
print(ans)