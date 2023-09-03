i = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    a = v // p
    b = v % p
    if l < b:
        b = l
    print(f'Case {i}: {a * l + b}')
    i += 1