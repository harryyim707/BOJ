arr = [int(input())for _ in range(10)]
s = arr[0]
for i in range(1, 10):
    if s + arr[i] <= 100:
        s += arr[i]
    elif abs(s+arr[i] - 100) > abs(s - 100):
        break
    else:
        s += arr[i]
        break
print(s)