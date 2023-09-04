g = int(input())
p = int(input())
gates = [0 for _ in range(g)]
planes = [int(input()) for _ in range(p)]
parent = {i: i for i in range(g + 1)}


def find_parent(x):
    if x == parent[x]:
        return x
    pa = find_parent(parent[x])
    parent[x] = pa
    return pa


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    parent[x] = y


c = 0
for plane in planes:
    x = find_parent(plane)
    if x == 0: break
    union(x, x - 1)
    c += 1
print(c)
