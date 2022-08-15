t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0
    if n == 0:
        cnt += 1
    for i in range(n, m+1):
        k = i
        while k > 0:
            if k % 10 == 0:
                cnt += 1
            k //= 10
    print(cnt)