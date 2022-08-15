n, k = map(int, input().split())
num = []
for i in range(1, k+1):
    num.append(int(str(n*i)[::-1]))
print(max(num))