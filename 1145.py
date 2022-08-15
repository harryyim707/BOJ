num = list(map(int, input().split()))
t = min(num)

while True:
    cnt = 0
    for i in range(5):
        if t % num[i] == 0:
            cnt += 1
    if cnt > 2:
        print(t)
        break
    t += 1