with open('10.txt', 'r') as file:
    data = [int(d) for d in file.read().splitlines()]
# Part 1
data = sorted(data.append(0))
data.append(data[-1] + 3)
d1 = 0
d3 = 0
for j in range(1, len(data)):
    d = data[j] - data[j - 1]
    if d == 1:
        d1 += 1
    elif d == 3:
        d3 += 1
print(d1 * d3)
# Part 2
consecgroups = []
j = 1
currgroup = []
while j < len(data):
    if data[j] - data[j - 1] == 3:
        if len(currgroup) >= 3:
            consecgroups.append(currgroup)
        currgroup = []
        j += 1
    else:
        if data[j - 1] not in currgroup:
            currgroup.append(data[j - 1])
        currgroup.append(data[j])
        j += 1
orders = 1
for group in consecgroups:
    n = len(group) - 2
    patterns = [bin(m).replace('0b', '').zfill(n) for m in range(2 ** n)]
    valid = len([pattern for pattern in patterns if '000' not in pattern])
    orders *= valid
print(orders)
