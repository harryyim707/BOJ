n = int(input())
seats = list(input())
cnt = 1
i = 0
while i < n:
    if i >= n:
        cnt += 1
        break
    if cnt >= n:
        cnt = n
        break
    if seats[i] == 'S':
        i += 1
        cnt += 1
    else:
        i += 2
        cnt += 1
print(cnt)