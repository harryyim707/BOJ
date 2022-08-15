arr = list(map(int, input()))
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#for i in arr:
#    num[i] += 1

for i in range(10):
    num[i] += arr.count(i)
s = (num[6]+num[9])%2+(num[6]+num[9])//2
num[6], num[9] = s, s
s = max(s, max(num))
print(s)