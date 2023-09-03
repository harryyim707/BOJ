n, k = map(int, input().split())
timeline = list(map(int, input().split()))
plugs = []
ans = 0
for i in range(k):
    if timeline[i] in plugs:
        continue
    if len(plugs) < n:
        plugs.append(timeline[i])
        continue

    latter = 0
    plugOut = 0
    for plug in plugs:
        if plug not in timeline[i:]:
            plugOut = plug
            break
        elif timeline[i:].index(plug) > latter:
            latter = timeline[i:].index(plug)
            plugOut = plug
    plugs[plugs.index(plugOut)] = timeline[i]
    ans += 1
print(ans)