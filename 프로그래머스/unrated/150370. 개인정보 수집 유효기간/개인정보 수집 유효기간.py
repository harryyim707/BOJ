def solution(today, terms, privacies):
    answer = []
    tod = list(map(int, today.split(".")))
    i = 0
    for priv in privacies:
        i += 1
        d, t = priv.split(" ")
        YYYY, MM, DD = map(int, d.split("."))
        for term in terms:
            t_type, due = term.split(" ")
            due = int(due)
            if t == t_type:
                MM += due
                if MM > 12:
                    YYYY += MM//12
                    MM %= 12
                    if MM == 0:
                        MM = 12
                        YYYY -= 1
                if YYYY < tod[0]:
                    answer.append(i)
                    break
                elif YYYY == tod[0]:
                    if MM < tod[1]:
                        answer.append(i)
                        break
                    elif MM == tod[1]:
                        if DD <= tod[2]:
                            answer.append(i)
                            break
    return answer