def solution(weights):
    answer = 0
    visit = [-1 for _ in range(4001)]
    same = [-1 for _ in range(1001)]
    for i in range(len(weights)):
        same[weights[i]] += 1
        answer += same[weights[i]]
        sameCnt = same[weights[i]]

        for j in range(2, 5):
            visit[weights[i] * j] += 1
            answer += (visit[weights[i] * j] - sameCnt)
    return answer