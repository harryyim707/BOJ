n, k = map(int, input().split())
num = list(map(int, input().split()))
s = []
s.append(sum(num[:k]))
for i in range(n-k):
    s.append(s[i]-num[i]+num[k+i])
print(max(s))