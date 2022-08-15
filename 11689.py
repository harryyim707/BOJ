def phi(k):
    res = k
    p = 2
    while p*p <= k:
        if k % p == 0:
            while k%p == 0:
                k //= p
            res *= (1.0-(1.0/float(p)))
        p += 1
    if k > 1:
        res *= (1.0 - (1.0/float(k)))
    return int(res)

n = int(input())
print(phi(n))