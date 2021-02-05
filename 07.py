import re
from collections import Counter

# Part 1
def RecCheck(mybag, father, containers, contdict, choices, checked):
    if mybag != father:
        if containers == []:
            containers = contdict[father]
        if mybag in containers:
            choices.append(father)
        else:
            for container in containers:
                if container in choices:
                    choices.append(father)
                    break
                else:
                    if container not in checked:
                        checked.append(container)
                        contents = contdict[container]
                        if mybag in contents:
                            if father not in choices:
                                choices.append(father)
                                break
                        else:
                            mybag, father, containers, contdict, choices, checked = RecCheck(mybag, father, contents, contdict, choices, checked)
    return mybag, father, containers, contdict, choices, checked

contentdict = {}
with open('07.txt', 'r') as file:
    for line in file:
        line = line.strip()
        container = re.sub(r'^(.+) bags contain.+', r'\1', line)
        bags = re.sub(r'.+contain(.+)\.', r'\1', line)
        contents = []
        if bags != ' no other bags':
            bags = bags.split(',')
            for bag in bags:
                contents.append(re.sub(r' \d+ (.+) bag(s*)', r'\1', bag))
        contentdict.update({container: contents})

choices = []
for item in contentdict:
    mybag, father, contents, contentdict, choices, checked = RecCheck('shiny gold', item, [], contentdict, choices, [])

print(len(Counter(choices)))

# Part 2
def Prod(v):
    p = 1
    for x in v:
        p *= x
    return p

def CountContent(color, dict, mult, counter):
    content = dict[color]
    for bag in content:
        color, qty = bag
        counter += mult * qty
        counter = CountContent(color, dict, mult * qty, counter)
    return counter

content = {}
with open('07.txt', 'r') as file:
    for line in file:
        line = line.strip()
        container = re.sub(r'^(.+) bags contain.+', r'\1', line)
        bags = re.sub(r'.+contain(.+)\.', r'\1', line)
        contents = []
        if bags != ' no other bags':
            bags = bags.split(',')
            for bag in bags:
                num = int(re.sub(r' (\d+) .+ bag(s*)', r'\1', bag))
                color = re.sub(r' \d+ (.+) bag(s*)', r'\1', bag)
                contents.append([color, num])
        content.update({container: contents})

print(CountContent('shiny gold', content, 1, 0))
# Wrong answers: 526381, 1269262, 1269260
