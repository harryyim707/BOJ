from signal import pthread_sigmask
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
p_sum = [0] * (n+1)
for i in range(n):
    p_sum[i+1] = p_sum[i]+arr[i]
l, ans = 0, sys.maxsize
for i in range(n+1):
    while(p_sum[i]-p_sum[l]) >= s:
        if p_sum[i]-p_sum[l+1] < s:
            break
        l+=1
    if p_sum[i]-p_sum[l] >= s:
        ans = min(ans, i-l)
        if ans == 1: break
print(ans) if ans != sys.maxsize else print(0)