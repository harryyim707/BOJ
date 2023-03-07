def solution(sequence):
    answer = 0
    length = len(sequence)
    dp = [0] * length
    dp[0] = sequence[0]
    if length == 1:
        return max(dp[0], dp[0]*-1)
    for i in range(1, length, 2):
        sequence[i] *= -1
    for i in range(1, length):
        dp[i] = max(dp[i-1]+sequence[i], sequence[i])
    answer = max(dp)
    for i in range(length):
        sequence[i] *= -1
    dp[0] = sequence[0]
    for i in range(1, length):
        dp[i] = max(dp[i-1]+sequence[i], sequence[i])
    answer = max(answer, max(dp))
    return answer