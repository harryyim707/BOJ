import heapq
n = int(input())
arr = []
for _ in range(n):
    numbers = list(map(int, input().split()))
    for number in numbers:
        if len(arr) < n:
            heapq.heappush(arr, number)
        else:
            if arr[0] < number:
                heapq.heappop(arr)
                heapq.heappush(arr, number)
print(arr[0])