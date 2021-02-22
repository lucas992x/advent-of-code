import copy

def Neighs3(coords):
    x, y, z = coords
    r = [-1, 0, 1]
    return [[x + i, y + j, z + k] for i in r for j in r for k in r if [i, j, k] != [0, 0, 0]]

def Cycle3(actives):
    activate = []
    deactivate = []
    inactives = []
    for cube in actives:
        neighs = Neighs3(cube)
        actneighs = 0
        for neigh in Neighs3(cube):
            if neigh in actives:
                actneighs += 1
            else:
                if neigh not in inactives:
                    inactives.append(neigh)
        if actneighs not in [2, 3]:
            deactivate.append(cube)
    for cube in inactives:
        neighs = Neighs3(cube)
        actneighs = 0
        for neigh in Neighs3(cube):
            if neigh in actives:
                actneighs += 1
        if actneighs  == 3:
            activate.append(cube)
    for cube in deactivate:
        actives.remove(cube)
    for cube in activate:
        actives.append(cube)
    return actives

def Neighs4(coords):
    x, y, z, w = coords
    r = [-1, 0, 1]
    return [[x + i, y + j, z + k, w + n] for i in r for j in r for k in r for n in r if [i, j, k, n] != [0, 0, 0, 0]]

def Cycle4(actives):
    activate = []
    deactivate = []
    inactives = []
    for cube in actives:
        neighs = Neighs4(cube)
        actneighs = 0
        for neigh in Neighs4(cube):
            if neigh in actives:
                actneighs += 1
            else:
                if neigh not in inactives:
                    inactives.append(neigh)
        if actneighs not in [2, 3]:
            deactivate.append(cube)
    for cube in inactives:
        neighs = Neighs4(cube)
        actneighs = 0
        for neigh in Neighs4(cube):
            if neigh in actives:
                actneighs += 1
        if actneighs  == 3:
            activate.append(cube)
    for cube in deactivate:
        actives.remove(cube)
    for cube in activate:
        actives.append(cube)
    return actives

with open('17.txt', 'r') as file:
    data = file.read().splitlines()

actives3 = []
actives4 = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '#':
            actives3.append([i, j, 0])
            actives4.append([i, j, 0, 0])

# Part 1
for j in range(6):
    actives3 = Cycle3(actives3)
print(len(actives3))

# Part 2 (pretty slow)
for j in range(6):
    actives4 = Cycle4(actives4)
print(len(actives4))
