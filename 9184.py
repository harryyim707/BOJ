import sys
dic = dict()


def w(a, b, c):
    global dic
    if (a, b, c) in dic.keys():
        return dic[(a, b, c)]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        dic[(20, 20, 20)] = w(20, 20, 20)
        return dic[(20, 20, 20)]
    elif a < b and b < c:
        dic[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dic[(a, b, c)]
    else:
        dic[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dic[(a, b, c)]


while True:
    a, b, c =list(map(int, sys.stdin.readline().split()))
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")