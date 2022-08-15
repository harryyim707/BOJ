N = int(input())
arr = list(map(int, input().split()))
num = 0
s = arr[0]
for i in range(1, N):
     num += s*arr[i]
     s += arr[i]
print(num)