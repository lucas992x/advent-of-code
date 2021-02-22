import copy

with open('11.txt', 'r') as file:
    data = file.read().splitlines()
grid = []
firstrow = ['.' for j in range(len(data[0]) + 2)]
grid.append(firstrow)
for line in data:
    newrow = ['.']
    for c in line:
        newrow.append(c)
    newrow.append('.')
    grid.append(newrow)
grid.append(firstrow)

# Part 1 (replace "while stable == True:" with "while stable == False:" to run it)
def Neighs1(seat, grid):
    row, col = seat
    if row in [0, len(grid) - 1] or col in [0, len(grid[0]) - 1]:
        return []
    else:
        return [grid[row - 1][col - 1], grid[row - 1][col], grid[row - 1][col + 1], grid[row][col - 1], grid[row][col + 1], grid[row + 1][col - 1], grid[row + 1][col], grid[row + 1][col + 1]]

def ApplyRules1(grd):
    occupy = []
    free = []
    for i in range(len(grd)):
        for j in range(len(grd[0])):
            neighs = Neighs1([i, j], grd)
            if grd[i][j] == 'L' and neighs.count('#') == 0:
                occupy.append([i, j])
            elif grd[i][j] == '#' and neighs.count('#') >= 4:
                free.append([i, j])
    for seat in occupy:
        grd[seat[0]][seat[1]] = '#'
    for seat in free:
        grd[seat[0]][seat[1]] = 'L'
    return grd

stable = False
while stable == True:
    newgrid = ApplyRules1(copy.deepcopy(grid))
    if newgrid == grid:
        stable = True
    grid = newgrid
occups = 0
for row in grid:
    occups += row.count('#')
print(occups)

# Part 2
def PrintGrid(grd):
    for row in grd:
        print(''.join(row))

def Neighs2(seat, grid):
    width = len(grid[0])
    height = len(grid)
    neighs = ['' for j in range(8)]
    # NW
    row, col = seat
    while row > 0 and col > 0:
        row -= 1
        col -= 1
        place = grid[row][col]
        if place != '.':
            neighs[0] = place
            break
    # N
    row, col = seat
    while row > 0:
        row -= 1
        place = grid[row][col]
        if place != '.':
            neighs[1] = place
            break
    # NE
    row, col = seat
    while row > 0 and col < width - 1:
        row -= 1
        col += 1
        place = grid[row][col]
        if place != '.':
            neighs[2] = place
            break
    # W
    row, col = seat
    while col > 0:
        col -= 1
        place = grid[row][col]
        if place != '.':
            neighs[3] = place
            break
    # E
    row, col = seat
    while col < width - 1:
        col += 1
        place = grid[row][col]
        if place != '.':
            neighs[4] = place
            break
    # SW
    row, col = seat
    while row < height - 1 and col > 0:
        row += 1
        col -= 1
        place = grid[row][col]
        if place != '.':
            neighs[5] = place
            break
    # S
    row, col = seat
    while row < height - 1:
        row += 1
        place = grid[row][col]
        if place != '.':
            neighs[6] = place
            break
    # SE
    row, col = seat
    while row < height - 1 and col < width - 1:
        row += 1
        col += 1
        place = grid[row][col]
        if place != '.':
            neighs[7] = place
            break
    return neighs
#print(Neighs2([1, 1], grid))

def ApplyRules2(grd):
    occupy = []
    free = []
    for i in range(len(grd)):
        for j in range(len(grd[0])):
            neighs = Neighs2([i, j], grd)
            if grd[i][j] == 'L' and neighs.count('#') == 0:
                occupy.append([i, j])
            elif grd[i][j] == '#' and neighs.count('#') >= 5:
                free.append([i, j])
    for seat in occupy:
        grd[seat[0]][seat[1]] = '#'
    for seat in free:
        grd[seat[0]][seat[1]] = 'L'
    return grd

#PrintGrid(grid)
stable = False
while stable == False:
    newgrid = ApplyRules2(copy.deepcopy(grid))
    #PrintGrid(newgrid)
    if newgrid == grid:
        stable = True
    grid = newgrid
occups = 0
for row in grid:
    occups += row.count('#')
print(occups)
