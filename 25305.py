n, k = map(int, input().split())
num = sorted(map(int, input().split()), reverse=True)
print(num[k-1])