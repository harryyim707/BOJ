n = int(input())
f = int(input())
n1 = (n//100)*100
for i in range(100):
    if (n1+i)%f == 0:
        n1 = str(n1+i)
        print(n1[-2::])
        break