n = int(input())
num = []
for i in range(1, n+1):
    x = i
    while x != 0:
        if x % 10 == 4 or x % 10 == 7:
            x //= 10
        else:
            break
    if x == 0:
        num.append(i)
print(num[-1])