from numpy import inf as inf
def solution(keymap, targets):
    answer = []
    for target in targets:
        cnt = 0
        for t in target:
            num = []
            for k in keymap:
                try:
                    num.append(k.index(t))
                except:
                    num.append(inf)
            cnt += (min(num)+1)
        if cnt == inf:
            answer.append(-1)
        else:
            answer.append(cnt)
    return answer