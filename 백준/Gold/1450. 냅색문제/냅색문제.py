import sys
input = sys.stdin.readline
n, c = map(int,input().split())
arr = list(map(int, input().split()))
a = arr[:n//2]
b = arr[n//2:]
a_sum, b_sum = [], []

def brute_force(ls, sumls, l, w):
    if l >= len(ls):
        sumls.append(w)
        return
    brute_force(ls, sumls, l+1, w)
    brute_force(ls, sumls, l+1, w+ls[l])


def binary_search(start, end, array, m):
    while start < end:
        mid = (start+end)//2
        if array[mid] <= m:
            start = mid+1
        else:
            end = mid
    return end


brute_force(a, a_sum, 0, 0)
brute_force(b, b_sum, 0, 0)
b_sum.sort()

cnt = 0
for i in a_sum:
    if c-i < 0:
        continue
    cnt += binary_search(0, len(b_sum), b_sum, c-i)
print(cnt)