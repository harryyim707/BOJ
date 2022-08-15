n = int(input())
isPrime = [True for _ in range(n+1)]
prime = []
for i in range(2, int(n**0.5)+1):
    if isPrime[i]:
        for j in range(i*i, n+1, i):
            isPrime[j] = False
for i in range(2, n+1):
    if isPrime[i]:
        prime.append(i)
l, r, now, cnt = 0, 0, 0, 0
length = len(prime)
while True:
    if now >= n:
        if now == n:
            cnt += 1
        now -= prime[l]
        l += 1
    elif r >= length:
        break
    else:
        now += prime[r]
        r += 1
print(cnt)
