import sys
n = int(sys.stdin.readline())
dic = [0] *1000001
dic[1] = 1
dic[2] = 2
for i in range(3, n+1):
    dic[i] = (dic[i-1]+dic[i-2])%15746
print(dic[n])