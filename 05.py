with open('05.txt', 'r') as file:
    data = file.read().splitlines()
# Part 1
ids = []
seats = []
for seat in data:
    rows = [*range(128)]
    cols = [*range(8)]
    for ch in seat[:7]:
        split = len(rows) // 2
        if ch == 'F':
            rows = rows[:split]
        else:
            rows = rows[split:]
    for ch in seat[7:]:
        split = len(cols) // 2
        if ch == 'L':
            cols = cols[:split]
        else:
            cols = cols[split:]
    seats.append([rows[0], cols[0]])
    ids.append(rows[0] * 8 + cols[0])
print(max(ids))
# Part 2
for r in range(128):
    for c in range(8):
        if [r, c] not in seats:
            id = r * 8 + c
            if id - 1 in ids and id + 1 in ids:
                print(id)
