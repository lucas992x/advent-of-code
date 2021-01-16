#input = '389125467'  # example
input = '952316487'  # my puzzle input

input = [int(n) for n in input]
next = {}
numcups = len(input)
for j in range(numcups):
    next.update({input[j]: input[(j + 1) % numcups]})

steps = 100
# this is needed only in part 2
start = len(input) + 1
until = 1000000
next.update({input[-1]: start})
for j in range(start, until):
    next.update({j: j + 1})
next.update({until: input[0]})
steps = 10000000

current = input[0]
numcups = len(next)
for j in range(steps):
    # pick next 3 cups
    picked = [next[current], next[next[current]], next[next[next[current]]]]
    # find destination cup
    dest = current - 1
    if dest == 0:
        dest = numcups
    while dest in picked:
        dest = dest - 1
        if dest == 0:
            dest = numcups
    # re-insert picked cups
    next.update({current: next[picked[2]]})
    next.update({picked[2]: next[dest]})
    next.update({dest: picked[0]})
    # select new current cup
    current = next[current]

''' Part 1
lst = [1]
while len(lst) < numcups:
    lst.append(next[lst[-1]])
print(''.join([str(n) for n in lst]))
'''
# Part 2
print(next[1] * next[next[1]])
# 648069867032 is too high
