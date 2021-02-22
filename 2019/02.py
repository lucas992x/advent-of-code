import re

vals = []
regex = r'(\d+)\-(\d+) (\w): (\w+)'
with open('02.txt', 'r') as file:
    for line in file:
        line = line.strip()
        min = int(re.sub(regex, r'\1', line))
        max = int(re.sub(regex, r'\2', line))
        letter = re.sub(regex, r'\3', line)
        password = re.sub(regex, r'\4', line)
        ''' Part 1
        lr = re.compile(letter)
        occs = len(lr.findall(password))
        if occs >= min and occs <= max:
            vals.append(line)
        '''
        if (password[min - 1] == letter and password[max - 1] != letter) or (password[min - 1] != letter and password[max - 1] == letter):
            vals.append(line)

print(len(vals))
