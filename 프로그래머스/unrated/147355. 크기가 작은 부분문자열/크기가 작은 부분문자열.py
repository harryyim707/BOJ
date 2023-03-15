def solution(t, p):
    answer = 0
    n = len(p)
    p = int(p)
    t_list = list(t)
    arr = []
    for i in range(len(t_list)-n+1):
        tmp = ""
        for j in range(i, i+n):
            tmp += t_list[j]
        if int(tmp) <= p:
            arr.append(tmp)
    answer = len(arr)
    return answer