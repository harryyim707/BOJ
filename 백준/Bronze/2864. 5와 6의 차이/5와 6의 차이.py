a, b = input().split()
a = list(a)
b = list(b)
for i in range(len(a)):
    if a[i] == '5' or a[i] == '6':
        a[i] = '6'
for i in range(len(b)):
    if b[i] == '5' or b[i] == '6':
        b[i] = '6'
maxSum = int(''.join(a)) + int(''.join(b))
for i in range(len(a)):
    if a[i] == '6':
        a[i] = '5'
for i in range(len(b)):
    if b[i] == '6':
        b[i] = '5'
minSum = int(''.join(a)) + int(''.join(b))
print(minSum, maxSum)