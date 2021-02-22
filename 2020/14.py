import re, copy

def NumToBin(num, length):
    return bin(int(num)).replace('0b', '').zfill(length)

with open('14.txt', 'r') as file:
    data = file.read().splitlines()

addresses = {}
for instr in data:
    if instr.startswith('mask'):
        mask = instr.replace('mask = ', '')
    else:
        ''' Part 1
        address = re.sub(r'mem\[(.+)\] = .+', r'\1', instr)
        value = NumToBin(re.sub(r'mem\[.+\] = (.+)', r'\1', instr), len(mask))
        written = '0b'
        for j in range(len(mask)):
            if mask[j] == 'X':
                written += value[j]
            else:
                written += mask[j]
        addresses.update({address: int(written, 2)})
        '''
        address = NumToBin(re.sub(r'mem\[(.+)\] = .+', r'\1', instr), len(mask))
        value = int(re.sub(r'mem\[.+\] = (.+)', r'\1', instr))
        towrite = '0b'
        for j in range(len(mask)):
            if mask[j] == '0':
                towrite += address[j]
            else:
                towrite += mask[j]
        n = towrite.count('X')
        patterns = [bin(m).replace('0b', '').zfill(n) for m in range(2 ** n)]
        for pattern in patterns:
            written = copy.deepcopy(towrite)
            for char in pattern:
                written = written.replace('X', char, 1)
            addresses.update({int(written, 2): value})
print(sum([addresses[address] for address in addresses]))
