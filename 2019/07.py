import itertools

with open('07.txt', 'r') as file:
    data = [int(d) for d in file.read().split(',')]

def get_value(data, mode, index):
    if mode == '0':
        value = data[data[index]]
    elif mode == '1':
        value = data[index]
    return value

# Part 1
def run1(data, phase, input):
    index = 0
    phased = False
    while data[index] != 99:
        instruction = str(data[index])
        while len(instruction) < 5:
            instruction = '0' + instruction
        opcode = int(instruction[-2:])
        parameters = instruction[:-2]
        # take input and store it (always in position mode)
        if opcode == 3:
            if phased == False:
                data[data[index + 1]] = phase
                phased = True
            else:
                data[data[index + 1]] = input
            index += 2
        # output something
        elif opcode == 4:
            value1 = get_value(data, parameters[2], index + 1)
            output = value1
            index += 2
        else:
            # first value
            value1 = get_value(data, parameters[2], index + 1)
            # second value
            value2 = get_value(data, parameters[1], index + 2)
            # address (always in position mode)
            address = data[index + 3]
            # write new value
            if opcode == 1:
                data[address] = value1 + value2
                index += 4
            elif opcode == 2:
                data[address] = value1 * value2
                index += 4
            elif opcode == 5:
                if value1:
                    index = value2
                else:
                    index += 3
            elif opcode == 6:
                if not value1:
                    index = value2
                else:
                    index += 3
            elif opcode == 7:
                if value1 < value2:
                    data[address] = 1
                else:
                    data[address] = 0
                index += 4
            elif opcode == 8:
                if value1 == value2:
                    data[address] = 1
                else:
                    data[address] = 0
                index += 4
    return output

# "output" argument is actually the initial input
def run1_5(data, phases, output):
    for j in range(5):
        output = run1(data[:], phases[j], output)
    return output

permutations = list(itertools.permutations([0, 1, 2, 3, 4]))
maxsignal = 0
for permutation in permutations:
    signal = run1_5(data[:], permutation, 0)
    if signal > maxsignal:
        maxsignal = signal

print(maxsignal)

# Part 2
def run2(data, index, inputs):
    finished = False
    while finished == False:
        instruction = str(data[index])
        while len(instruction) < 5:
            instruction = '0' + instruction
        opcode = int(instruction[-2:])
        parameters = instruction[:-2]
        # halt
        if opcode == 99:
            finished = True
            output = -666  # random low value
        # take input and store it (always in position mode)
        elif opcode == 3:
            data[data[index + 1]] = inputs[0]
            inputs.remove(inputs[0])
            index += 2
        # output something
        elif opcode == 4:
            value1 = get_value(data, parameters[2], index + 1)
            output = value1
            index += 2
            break
        else:
            # first value
            value1 = get_value(data, parameters[2], index + 1)
            # second value
            value2 = get_value(data, parameters[1], index + 2)
            # address (always in position mode)
            address = data[index + 3]
            # write new value
            if opcode == 1:
                data[address] = value1 + value2
                index += 4
            elif opcode == 2:
                data[address] = value1 * value2
                index += 4
            elif opcode == 5:
                if value1:
                    index = value2
                else:
                    index += 3
            elif opcode == 6:
                if not value1:
                    index = value2
                else:
                    index += 3
            elif opcode == 7:
                if value1 < value2:
                    data[address] = 1
                else:
                    data[address] = 0
                index += 4
            elif opcode == 8:
                if value1 == value2:
                    data[address] = 1
                else:
                    data[address] = 0
                index += 4
    return data, inputs, output, index, finished

# "output" argument is actually the initial input
def run2_5(data, phases, output):
    data = [data[:], data[:], data[:], data[:], data[:]]
    indexes = [0, 0, 0, 0, 0]
    inputs = [[phases[0], 0], [phases[1]], [phases[2]], [phases[3]], [phases[4]]]
    finished = False
    j = 0
    while finished == False or j % 5 != 4:
        data[j % 5], inputs[j % 5], output, index, finished = run2(data[j % 5], indexes[j % 5], inputs[j % 5])
        indexes[j % 5] = index
        j += 1
        inputs[j % 5].append(output)
        if finished == False:
            thrust = output
    return thrust

permutations = list(itertools.permutations([5, 6, 7, 8, 9]))
maxsignal = 0
for permutation in permutations:
    signal = run2_5(data[:], permutation, 0)
    if signal > maxsignal:
        maxsignal = signal

print(maxsignal)
