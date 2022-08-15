n, m = map(int, input().split())
k = list(map(int, input().split()))
num = [False]*(n+1)
for i in k:
    for j in range(i, n+1, i):
        if not num[j]:
            num[j] = True
print(sum(i if num[i] else 0 for i in range(n+1)))