def solution(n, m, section):
    answer = 0
    tmp = [0] * (n+1)
    t = section[0]
    tmp[:t] = [1]*t
    for idx in section:
        if tmp[idx] != 1:
            answer += 1
            if idx+m-1 <= n:
                tmp[idx:idx+m] = [1]*m
            else:
                tmp[idx:n] = [1] * (n-idx+1)
    return answer