from heapq import heappush, heappop
def timetoint(string):
    h, m = string.split(":")
    return int(h)*60+int(m)
def solution(book_time):
    heap = []
    last_out = [-10]
    for i,o in book_time:
        i, o = timetoint(i), timetoint(o)
        heappush(heap, (i, o))
    while heap:
        now_in, now_out = heappop(heap)
        if now_in >= last_out[0]+10:
            heappop(last_out)
            heappush(last_out, now_out)
        else:
            heappush(last_out, now_out)
    return len(last_out)