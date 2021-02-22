def run(data, input):
    index = 0
    outputs = []
    while data[index] != 99:
        instruction = str(data[index])
        while len(instruction) < 5:
            instruction = '0' + instruction
        opcode = int(instruction[-2:])
        parameters = instruction[:-2]
        # take input and store it (always in position mode)
        if opcode == 3:
            data[data[index + 1]] = input
            index += 2
        # output something
        elif opcode == 4:
            if parameters[2] == '0':
                value1 = data[data[index + 1]]
            else:
                value1 = data[index + 1]
            outputs.append(value1)
            index += 2
        else:
            # first value
            if parameters[2] == '0':
                value1 = data[data[index + 1]]
            else:
                value1 = data[index + 1]
            # second value
            if parameters[1] == '0':
                value2 = data[data[index + 2]]
            else:
                value2 = data[index + 2]
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
    return outputs

with open('05.txt', 'r') as file:
    data = [int(d) for d in file.read().split(',')]

# Part 1
print(run(data[:], 1))

# Part 2
print(run(data[:], 5))
