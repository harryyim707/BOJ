n = int(input())
a, b, c = 0, 0, 0
for i in range(1, n + 1):
    x = str(i)
    a += x.count("3")
    b += x.count("6")
    c += x.count("9")
print(a + b + c)
