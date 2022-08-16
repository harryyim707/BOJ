k = int(input())
dir = {i:0 for i in range(1, 5)}
w, h = [], []
for _ in range(6):
    a, b = map(int, input().split())
    dir[a] += 1
    if a == 1 or a == 2:
         w.append(b)
    elif a == 3 or a == 4:
         h.append(b)
wid = w.index(max(w))
hid = h.index(max(h))
if dir[1] == 2 and dir[3] == 2:
    s = w[wid - 2] * h[hid - 1]
elif dir[1] == 2 and dir[4] == 2:
    s = w[wid - 1] * h[hid - 2]
elif dir[2] == 2 and dir[3] == 2:
    s = w[wid - 1] * h[hid - 2]
elif dir[2] == 2 and dir[4] == 2:
    s = w[wid - 2] * h[hid - 1]
print((max(w) * max(h) - s) * k)