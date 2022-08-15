import sys
s = list(sys.stdin.readline().rstrip().split('-'))
result = 0
for i in s[0].split('+'):
    result += int(i)
for i in s[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)