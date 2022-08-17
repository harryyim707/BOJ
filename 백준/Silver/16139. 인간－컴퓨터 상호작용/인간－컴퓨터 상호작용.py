import sys
input = sys.stdin.readline
s = input().strip()
arr = [[0 for _ in range(26)]for _ in range(len(s))]
arr[0][ord(s[0])-97] = 1
q = int(input())
for i in range(1, len(s)):
    arr[i][ord(s[i])-97] = 1
    for j in range(26):
        arr[i][j] += arr[i-1][j]
for _ in range(q):
    alpha, l, r = input().split()
    l, r = int(l), int(r)
    if l > 0:
        res = arr[r][ord(alpha)-97]-arr[l-1][ord(alpha)-97]
    else:
        res = arr[r][ord(alpha)-97]
    print(res)

    