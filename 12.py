getmovs = {
'N': [0, 1],
'S': [0, -1],
'E': [1, 0],
'W': [-1, 0],
}
dirs = ['N', 'E', 'S', 'W']

with open('12.txt', 'r') as file:
    movs = file.read().splitlines()
''' Part 1
def MoveShip(pos, mov):
    x, y = pos
    dir = mov[0]
    dist = int(mov[1:])
    movx, movy = getmovs[dir]
    return [x + movx * dist, y + movy * dist]

def RotateShip(dir, rot):
    if rot.startswith('L'):
        mult = -1
    else:
        mult = 1
    steps = int(rot[1:]) // 90
    return dirs[(dirs.index(dir) + mult * steps) % 4]

pos = [0, 0]
dir = 'E'
for mov in movs:
    if mov.startswith('F'):
        pos = MoveShip(pos, '{}{}'.format(dir, mov[1:]))
    elif mov.startswith('L') or mov.startswith('R'):
        dir = RotateShip(dir, mov)
    else:
        pos = MoveShip(pos, mov)
print(sum([abs(j) for j in pos]))
'''
def MoveShip(pos, wp, times):
    x, y = pos
    movx, movy = wp
    return [x + movx * times, y + movy * times]

def MoveWp(wp, move):
    x, y = wp
    dir = move[0]
    dist = int(move[1:])
    movx, movy = getmovs[dir]
    return [x + movx * dist, y + movy * dist]

def RotateWp(wp, rot):
    x, y = wp
    if rot.startswith('L'):
        multx = 1
        multy = -1
    else:
        multx = -1
        multy = 1
    return [y * multy, x * multx]

pos = [0, 0]
wp = [10, 1]
for mov in movs:
    if mov.startswith('F'):
        pos = MoveShip(pos, wp, int(mov[1:]))
    elif mov.startswith('L') or mov.startswith('R'):
        for j in range(int(mov[1:]) // 90):
            wp = RotateWp(wp, mov)
    else:
        wp = MoveWp(wp, mov)
print(sum([abs(j) for j in pos]))
