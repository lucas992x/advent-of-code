with open('03.txt', 'r') as file:
    grid = file.read().splitlines()

nrows = len(grid)
ncols = len(grid[0])
#movs = [[3, 1]]  # Part 1
movs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]  # Part 2
trees = 1
for mov in movs:
    hmov, vmov = mov
    parttrees = 0
    pos = [0, 0]
    while pos[0] < nrows - 1:
        pos = [(pos[0] + vmov) % nrows, (pos[1] + hmov) % ncols]
        if grid[pos[0]][pos[1]] == '#':
            parttrees += 1
    trees *= parttrees
print(trees)
