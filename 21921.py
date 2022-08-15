n, x = map(int, input().split())
visitor = list(map(int, input().split()))
cnt = 1
s = sum(visitor[:x])
res = s
for i in range(n-x):
    s -= visitor[i]
    s += visitor[i+x]
    if res == s:
        cnt += 1
    if res < s:
        res = s
        cnt = 1
if res == 0:
    print("SAD")
else:
    print(res)
    print(cnt)