def run(data):
    index = 0
    while data[index] != 99:
        value1 = data[data[index + 1]]
        value2 = data[data[index + 2]]
        address = data[index + 3]
        if data[index] == 1:
            data[address] = value1 + value2
        elif data[index] == 2:
            data[address] = value1 * value2
        index += 4
    return data[0]

with open('02.txt', 'r') as file:
    data = [int(d) for d in file.read().split(',')]

# Part 1
print(run([data[0], 12, 2, *data[3:]]))

# Part 2
for noun in range(100):
    for verb in range(100):
        if run([data[0], noun, verb, *data[3:]]) == 19690720:
            print(100 * noun + verb)
            break
    else:
        continue
    break
