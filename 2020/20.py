import re
from math import sqrt

class Tile:
    def __init__(self, text):
        self.id = int(re.sub(r'Tile (\d+):', r'\1', text.splitlines()[0]))
        self.content = re.sub(r'Tile \d+:\n', '', text)
        self.GetBorders()
        self.matches = []
        self.nummatches = 0

    def GetBorders(self):
        lines = self.content.splitlines()
        borderN = lines[0]
        borderE = ''.join([line[-1] for line in lines])
        borderS = lines[-1]
        borderW = ''.join([line[0] for line in lines])
        self.borders = [borderN, borderE, borderS, borderW]

    def AddMatch(self, match):
        self.matches.append(match)
        self.nummatches += 1

    def FlipH(self):
        # update content
        self.content = '\n'.join([line[::-1] for line in self.content.splitlines()])
        self.GetBorders()
        # update matches
        newmatches = []
        for match in self.matches:
            if match[0] in [1, 3]:
                newmatch = [4 - match[0], match[1]]
                newmatches.append(newmatch)
            else:
                newmatches.append(match)
        self.matches = newmatches

    def FlipV(self):
        # update content
        self.content = '\n'.join(self.content.splitlines()[::-1])
        self.GetBorders()
        # update matches
        newmatches = []
        for match in self.matches:
            if match[0] in [0, 2]:
                newmatch = [2 - match[0], match[1]]
                newmatches.append(newmatch)
            else:
                newmatches.append(match)
        self.matches = newmatches

    # clockwise rotation
    def Rotate(self, degrees):
        if degrees == 90:
            # update content
            lines = self.content.splitlines()
            self.content = ''
            for j in range(len(lines)):
                self.content += ''.join([line[j] for line in lines[::-1]]) + '\n'
            self.content = self.content.strip()
            # update matches
            newmatches = []
            for match in self.matches:
                newmatches.append([(match[0] + 1) % 4, match[1]])
            self.matches = newmatches
        elif degrees == 180:
            # update content
            self.content = '\n'.join([line[::-1] for line in self.content.splitlines()[::-1]])
            # update matches
            newmatches = []
            for match in self.matches:
                newmatches.append([(match[0] + 2) % 4, match[1]])
            self.matches = newmatches
        elif degrees == 270:
            # update content
            lines = self.content.splitlines()
            self.content = ''
            for j in range(len(lines)):
                self.content += ''.join([line[len(lines) - 1 - j] for line in lines]) + '\n'
            self.content = self.content.strip()
            # update matches
            newmatches = []
            for match in self.matches:
                newmatches.append([(match[0] + 3) % 4, match[1]])
            self.matches = newmatches
        self.GetBorders()

    def RemoveBorders(self):
        self.content = re.sub(r'\n.(.+).', r'\n\1', self.content)
        self.content = re.sub(r'^(.+)\n', r'', self.content)
        self.content = re.sub(r'\n(.+)$', r'', self.content)

def CompareBorders(tile1, tile2):
    match = None
    for border1 in tile1.borders:
        for border2 in tile2.borders:
            if border1 == border2 or border1 == border2[::-1]:
                match = [tile1.borders.index(border1), tile2.borders.index(border2)]
    return match

# Part 1
with open('20.txt', 'r') as file:
    data = file.read().split('\n\n')

tiles = [Tile(d) for d in data]
for j in range(len(tiles)):
    for k in range(len(tiles)):
        if j != k:
            match = CompareBorders(tiles[j], tiles[k])
            if match is not None:
                match1 = [match[0], tiles[k].id]
                if match1 not in tiles[j].matches:
                    tiles[j].AddMatch(match1)
                match2 = [match[1], tiles[j].id]
                if match2 not in tiles[k].matches:
                    tiles[k].AddMatch(match2)

prod = 1
corners = []
for tile in tiles:
    if tile.nummatches == 2:
        corners.append(tile)
        prod *= tile.id
print(prod)

# Part 2
first = corners[0]
while [m[0] for m in first.matches] not in [[1, 2], [2, 1]]:
    first.Rotate(90)

first.RemoveBorders()
puzzle = [first]
tot = len(tiles)
while len(puzzle) < tot:
    last = puzzle[-1]
    if [m for m in last.matches if m[0] == 1] == []:
        current = [i for i in puzzle if [m for m in i.matches if m[0] == 3] == []][-1]
        compare = [2, 0]
    else:
        current = last
        compare = [1, 3]
    nextid = [m[1] for m in current.matches if m[0] == compare[0]][0]
    next = [t for t in tiles if t.id == nextid][0]
    while [m[0] for m in next.matches if m[1] == current.id][0] != compare[1]:
        next.Rotate(90)
    if current.borders[compare[0]] != next.borders[compare[1]]:
        if compare[0] == 1:
            next.FlipV()
        else:
            next.FlipH()
    next.RemoveBorders()
    puzzle.append(next)

width = int(sqrt(len(puzzle)))
rows = [puzzle[j:j + width] for j in range(0, tot, width)]
image = ''
for row in rows:
    pieces = [tile.content.splitlines() for tile in row]
    for j in range(len(pieces[0])):
        image += ''.join([piece[j] for piece in pieces]) + '\n'

image = Tile('Tile 0:\n' + image)  # to re-use rotate and flip functions
imgwidth = len(image.content.splitlines())
monster = '..................#.\n#....##....##....###\n.#..#..#..#..#..#...'
monsterwidth = len(monster.splitlines()[0])
regexes = r''
for j in range(imgwidth - monsterwidth + 1):
    if j == 0:
        right = r''
        left = r'.*'
    elif j == imgwidth - monsterwidth:
        right = r'.*'
        left = r''
    else:
        right = r'.{' + str(j) + r'}'
        left = r'.{' + str(imgwidth - j - monsterwidth) + r'}'
    sep = r'\n'.join([right, left])
    regexes += sep.join(monster.splitlines()) + r'|'
regexes = regexes.strip('|')
rots = 0
flips = 0
while not re.search(regexes, image.content):
    if rots == 3:
        if flips == 1:
            print('No match!')
            break
        else:
            image.FlipH()
            rots = 0
            flips = 1
    else:
        image.Rotate(90)
        rots += 1

monsters = 0
for regex in regexes.split('|'):
    monsters += len(re.findall(regex, image.content))
print(image.content.count('#') - monsters * monster.count('#'))
