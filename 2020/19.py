import re, copy

with open('19.txt', 'r') as file:
    data = file.read().split('\n\n')

rules = {}
for line in data[0].splitlines():
    num = int(re.sub(r'^(\d+): .+$', r'\1', line))
    if '"' in line:
        rule = re.sub(r'^.+"(\w)"$', r'\1', line)
        rules.update({num: rule})
    else:
        options = re.sub(r'^.+: (.+)$', r'\1', line).split('|')
        nums = []
        for option in options:
            nums.append([int(n) for n in option.strip().split(' ')])
        rules.update({num: nums})

strings = [num for num in rules if type(rules[num]) == type('a')]
while len(strings) < len(rules):
    check = copy.deepcopy(rules)
    for num in rules:
        rule = rules[num]  # examples: 'abac', ['aab', 'aba'], ['aab', [1, 2]], [[1, 2], [3, 2]]
        if type(rule) != type('a'):
            if len([r for r in rule if type(r) == type('a')]) == len(rule):
                rule = '({})'.format('|'.join(rule))
                rules.update({num: rule})
                strings.append(num)
            else:
                for i in range(len(rule)):
                    for j in range(len(rule[i])):
                        if rule[i][j] in strings:
                            rule[i][j] = rules[rule[i][j]]
                    if len([p for p in rule[i] if type(p) == type('a')]) == len(rule[i]):
                        rule[i] = ''.join(rule[i])
                rules.update({num: rule})

messages = data[1].splitlines()

# Part 1
counter = 0
for message in messages:
    if re.search('^{}$'.format(rules[0]), message):
        counter += 1
print(counter)

# Part 2
rules.update({8: '({})+'.format(rules[42])})
longest = max([len(m) for m in messages])
newrules = [j * rules[42] + j * rules[31] for j in range(1, longest // 2)]
rules.update({11: '({})'.format('|'.join(newrules))})
rules.update({0: rules[8] + rules[11]})
counter = 0
for message in messages:
    if re.search('^{}$'.format(rules[0]), message):
        counter += 1
print(counter)
