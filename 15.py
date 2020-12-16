#data = [0, 3, 6]  # example
data = [1, 20, 8, 12, 0, 14]  # puzzle input
occs = {}
last = {}
prev = {}
for item in data:
    occs.update({item: data.count(item)})
    last.update({item: data.index(item)})

current = data[-1]
for j in range(len(data), 30000000):  # 2020 for part 1
    occscurr = occs.get(current, 0)
    if occscurr > 1:
        current = last[current] - prev[current]
        occscurrent = occs.get(current, 0)
        if occscurrent > 0:
            occs.update({current: occscurrent + 1})
            prev.update({current: last[current]})
            last.update({current: j})
        else:
            occs.update({current: 1})
            last.update({current: j})
    else:
        current = 0
        occs.update({0: occs.get(0, 0) + 1})
        prev.update({0: last[0]})
        last.update({0: j})
print(current)
