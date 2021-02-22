import re

def CheckRange(num, rng):
    if (rng[1] <= num and num <= rng[2]) or (rng[3] <= num and num <= rng[4]):
        return True
    else:
        return False

with open('16.txt', 'r') as file:
    data = file.read().split('\n\n')

ranges = [[re.sub(r'^(.+):.+$', r'\1', line)] + [int(n) for n in re.findall(r'\d+', line)] for line in data[0].split('\n')]
tickets = [[int(n) for n in ticket.split(',')] for ticket in data[2].splitlines()[1:]]
tser = 0
valids = []
for ticket in tickets:
    validticket = True
    for num in ticket:
        validnum = False
        for rng in ranges:
            if CheckRange(num, rng):
                validnum = True
                break
        if validnum == False:
            tser += num
            validticket = False
    if validticket == True:
        valids.append(ticket)
print(tser)  # Part 1

tfields = [[v[j] for v in valids] for j in range(len(valids[0]))]
fpossibs = []
for tfield in tfields:
    fpossib = []
    for rng in ranges:
        if [CheckRange(num, rng) for num in tfield] == [True] * len(tfield):
            fpossib.append(1)
        else:
            fpossib.append(0)
    fpossibs.append(fpossib)

while sum([sum(f) for f in fpossibs]) > len(fpossibs):
    for fpossib in fpossibs:
        if fpossib.count(1) == 1:
            index = fpossib.index(1)
            for fp in fpossibs:
                if fp != fpossib:
                    fp[index] = 0

myticket = [int(n) for n in data[1].replace('your ticket:\n', '').split(',')]
prod = 1
for j in range(len(fpossibs)):
    if fpossibs[j].index(1) < 6:
        prod *= myticket[j]
print(prod)  # Part 2
