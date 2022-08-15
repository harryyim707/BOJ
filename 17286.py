x, y = [] , []
for i in range(4):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

def f(i, j):
    return ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5

print(int(min(
    f(0, 1) + f(1, 2) + f(2, 3),
    f(0, 1) + f(1, 3) + f(2, 3),
    f(0, 2) + f(2, 1) + f(1, 3),
    f(0, 2) + f(2, 3) + f(1, 3),
    f(0, 3) + f(3, 1) + f(1, 2),
    f(0, 3) + f(3, 2) + f(1, 2)
    )))