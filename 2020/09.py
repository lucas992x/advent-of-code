with open('09.txt', 'r') as file:
    data = [int(n) for n in file.read().splitlines()]
# Part 1
preamble = 25
for k in range(preamble, len(data)):
    exists = False
    for i in range(k - preamble, k):
        for j in range(i, k):
            if data[i] + data[j] == data[k]:
                exists = True
    if exists == False:
        print(data[k])
        break
# Part 2
index = data.index(error)
for i in range(index):
    for j in range(i, index):
        items = [data[k] for k in range(i, j + 1)]
        if sum(items) == error:
            print(min(items) + max(items))
            break
