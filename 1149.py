import sys
n = int(sys.stdin.readline())
house = [[0 for i in range(3)]for j in range(1001)]

house[1] = list(map(int, sys.stdin.readline().split()))

for i in range(2, n+1):
    R, G, B = list(map(int, sys.stdin.readline().split()))
    house[i][0] = min(house[i-1][1]+R, house[i-1][2]+R)
    house[i][1] = min(house[i-1][0]+G, house[i-1][2]+G)
    house[i][2] = min(house[i-1][0]+B, house[i-1][1]+B)

answer = min(house[n][0], house[n][1])
answer = min(answer, house[n][2])
print(answer)