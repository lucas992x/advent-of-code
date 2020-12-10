import re

def Run(data):
    executed = [False] * len(data)
    accum = 0
    j = 0
    exit = False
    ended = False
    while exit == False:
        if j >= len(data):
            ended = True
            exit = True
        else:
            if executed[j] == True:
                exit = True
            else:
                executed[j] = True
                instr = data[j]
                if instr.startswith('acc'):
                    accum += int(re.sub(r'acc (.+)$', r'\1', instr))
                    j += 1
                elif instr.startswith('jmp'):
                    j += int(re.sub(r'jmp (.+)$', r'\1', instr))
                else:
                    j += 1
    return accum, ended

with open('08.txt', 'r') as file:
    data = file.read().splitlines()

''' Part 1
accum, ended = Run(data)
print(accum)
'''
for j in range(len(data)):
    if re.search(r'(jmp|nop)', data[j]):
        newdata = [d for d in data]
        if data[j].startswith('nop'):
            newdata[j] = newdata[j].replace('nop', 'jmp')
        else:
            newdata[j] = newdata[j].replace('jmp', 'nop')
        accum, ended = Run(newdata)
        if ended == True:
            print(accum)
