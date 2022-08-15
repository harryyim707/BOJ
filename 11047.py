import sys
n, k = map(int,sys.stdin.readline().split())
coin_list = []
for _ in range(n):
    coin_list.append(int(sys.stdin.readline()))
coin_list.sort(reverse=True)
cnt = 0
for coin in coin_list:
    if k - coin >= 0:
        cnt += k // coin
        k %= coin
print(cnt)