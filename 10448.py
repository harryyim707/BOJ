t = int(input())
T = []
i = 1
while True:
    num = (i*(i+1))//2
    if num > 1000:
        break
    T.append(num)
    i += 1


def tri(n):
    for i in range(len(T)):
        for j in range(len(T)):
            for k in range(len(T)):
                if T[i]+T[j]+T[k] == n:
                    return 1
    return 0

    
for _ in range(t):
    k = int(input())
    print(tri(k))