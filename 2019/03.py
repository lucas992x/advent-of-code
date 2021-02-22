def getnodes(path):
    nodes = [[0, 0]]
    moves = path.split(',')
    for move in moves:
        direction = move[0]
        length = int(move[1:])
        if direction == 'L':
            nodes.append([nodes[-1][0] - length, nodes[-1][1]])
        elif direction == 'R':
            nodes.append([nodes[-1][0] + length, nodes[-1][1]])
        elif direction == 'U':
            nodes.append([nodes[-1][0], nodes[-1][1] + length])
        elif direction == 'D':
            nodes.append([nodes[-1][0], nodes[-1][1] - length])
    return nodes

def search_intersection(seg1, seg2):
    A, B = seg1
    C, D = seg2
    if A[0] == B[0]:
        dir1 = 'V'
    else:
        dir1 = 'H'
    if C[0] == D[0]:
        dir2 = 'V'
    else:
        dir2 = 'H'
    if dir1 == dir2:
        intersection = None
    else:
        if dir1 == 'H':
            interval1 = range(min([A[0], B[0]]), max([A[0], B[0]]) + 1)
            interval2 = range(min([C[1], D[1]]), max([C[1], D[1]]) + 1)
            if C[0] in interval1 and A[1] in interval2:
                intersection = [C[0], A[1]]
            else:
                intersection = None
        else:
            interval1 = range(min([C[0], D[0]]), max([C[0], D[0]]) + 1)
            interval2 = range(min([A[1], B[1]]), max([A[1], B[1]]) + 1)
            if A[0] in interval1 and C[1] in interval2:
                intersection = [A[0], C[1]]
            else:
                intersection = None
    return intersection

# Part 1
with open('03.txt', 'r') as file:
    path1, path2 = file.read().splitlines()

nodes1 = getnodes(path1)
nodes2 = getnodes(path2)
intersections = []
for i in range(len(nodes1) - 1):
    for j in range(len(nodes2) - 1):
        seg1 = [nodes1[i], nodes1[i + 1]]
        seg2 = [nodes2[j], nodes2[j + 1]]
        intersection = search_intersection(seg1, seg2)
        if intersection is not None and intersection != [0, 0]:
            intersections.append(intersection)

print(min([abs(intersection[0]) + abs(intersection[1]) for intersection in intersections]))

# Part 2
def get_steps(intersection, nodes):
    steps = 0
    for j in range(len(nodes) - 1):
        A = nodes[j]
        B = nodes[j + 1]
        if A[0] == B[0] and intersection[0] == A[0] and intersection[1] >= min([A[1], B[1]]) and intersection[1] <= max([A[1], B[1]]):
            steps += abs(intersection[1] - A[1])
            break
        elif A[1] == B[1] and intersection[1] == A[1] and intersection[0] >= min([A[0], B[0]]) and intersection[0] <= max([A[0], B[0]]):
            steps += abs(intersection[0] - A[0])
            break
        else:
            steps += abs(A[0] - B[0]) + abs(A[1] - B[1])
    return steps

steps = []
for intersection in intersections:
    steps1 = get_steps(intersection, nodes1)
    steps2 = get_steps(intersection, nodes2)
    steps.append(steps1 + steps2)

print(min(steps))
