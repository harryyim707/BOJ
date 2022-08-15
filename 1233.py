s1, s2, s3 = map(int, input().split())
num = [0] * (s1+s2+s3+1) #changed the list index to run as the sum of 3 dices
for i in range(1, s1+1): #forgot to start from 1
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            num[i+j+k] += 1
print(num.index(max(num)))