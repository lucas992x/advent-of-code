# Part 1
with open('01.txt', 'r') as file:
    data = [int(line) for line in file.read().splitlines()]

print(sum([num // 3 - 2 for num in data]))

# Part 2
tot = 0
for num in data:
    num = num // 3 - 2
    while num > 0:
        tot += num
        num = num // 3 - 2

print(tot)
