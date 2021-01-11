singlemove = {
'e': [1, 0],
'w': [-1, 0],
'ne': [0, 1],
'sw': [0, -1],
'nw': [-1, 1],
'se': [1, -1],
}

def Move(pos, movements):
    while len(movements) > 0:
        if movements[0] in ['e', 'w']:
            n = 1
        else:
            n = 2
        move = singlemove[movements[0:n]]
        pos = [pos[0] + move[0], pos[1] + move[1]]
        movements = movements[n:]
    return pos

def Neighs(pos):
    return [[pos[0] + singlemove[n][0], pos[1] + singlemove[n][1]] for n in singlemove]

def NumBlackNeighs(pos, blacks):
    return len([n for n in Neighs(pos) if n in blacks])

def GetWhites(blacks):
    whites = []
    for black in blacks:
        whiteneighs = Neighs(black)
        for neigh in whiteneighs:
            if neigh not in whites + blacks:
                whites.append(neigh)
    return whites

with open('24.txt', 'r') as file:
    data = file.read().splitlines()

# Part 1
blacks = []
for movements in data:
    finish = Move([0, 0], movements)
    if finish in blacks:
        blacks.remove(finish)
    else:
        blacks.append(finish)
print(len(blacks))

# Part 2
for j in range(100):
    whites = GetWhites(blacks)
    fliptowhite = []
    fliptoblack = []
    for black in blacks:
        if NumBlackNeighs(black, blacks) not in [1, 2]:
            fliptowhite.append(black)
    for white in whites:
        if NumBlackNeighs(white, blacks) == 2:
            fliptoblack.append(white)
    for ftw in fliptowhite:
        blacks.remove(ftw)
    for ftb in fliptoblack:
        blacks.append(ftb)
print(len(blacks))
