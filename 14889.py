import sys
from itertools import combinations
n = int(sys.stdin.readline())
s = []
for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

available = list(combinations([i for i in range(n)], n//2))
start = []
link = []

for m in range(len(available)//2):
    coor_1 = list(combinations(available[m], 2))
    coor_2 = list(combinations(available[len(available)-1-m], 2))
    score_s = 0
    score_l = 0
    for k in coor_1:
        i = k[0]
        j = k[1]
        score_s = score_s + s[i][j] + s[j][i]
    start.append(score_s)
    for l in coor_2:
        i = l[0]
        j = l[1]
        score_l = score_l + s[i][j] + s[j][i]
    link.append(score_l)
result = []
for i in range(len(start)):
    result.append(abs(start[i] - link[i]))
print(min(result))