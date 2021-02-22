alphabet = 'abcdefghijklmnopqrstuvwxyz'

with open('06.txt', 'r') as file:
    groups = file.read().split('\n\n')

tot = 0
for group in groups:
    ''' Part 1
    score = 0
    for letter in alphabet:
        if letter in group:
            score += 1
    tot += score
    '''
    group = group.strip('\n')
    if '\n' not in group:
        tot += len(group)
    else:
        people = group.split('\n')
        score = 0
        for letter in alphabet:
            occs = [1 for person in people if letter in person]
            if len(occs) == len(people):
                score += 1
        tot += score
print(tot)
