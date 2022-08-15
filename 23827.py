n = int(input())
arr = list(map(int, input().split()))
sub = 0
s = 0
for i in range(n):
    s += arr[i]
    sub += arr[i]*arr[i]
print(((s*s-sub)//2) % 1000000007)