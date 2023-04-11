def solution(sequence, k):
    sequence = [0] + sequence
    n = len(sequence)
    arr = [0] * n
    for i in range(1, n):
        arr[i] = arr[i-1] + sequence[i]
    i, j = 1, 1
    win = 1000000
    a, b = -1, -1
    while i <= j < n:
        check = arr[j] - arr[i-1]
        if check < k:
            j += 1
        elif check == k:
            if win > j-i:
                win = j-i
                a, b = i, j
            j += 1
        else:
            i += 1
    return [a-1, b-1]