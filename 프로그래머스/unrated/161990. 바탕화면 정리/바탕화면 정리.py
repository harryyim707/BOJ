def solution(wallpaper):
    answer = []
    lux = 51
    luy = 51
    rdx = -1
    rdy = -1
    length = len(wallpaper)
    for i in range(length):
        row = list(wallpaper[i])
        j = 0
        if "#" in row:
            if lux >= i:
                lux = i
            if rdx <= i:
                rdx = i+1
            while j<len(row):
                if row[j] == "#":
                    if luy >= j:
                        luy = j
                    if rdy <= j:
                        rdy = j+1
                j+=1
    answer.extend([lux, luy, rdx, rdy])
    return answer