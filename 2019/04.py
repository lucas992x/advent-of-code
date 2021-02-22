import re

# This code is horrible, I was trying all before finding the (obviously stupid) mistake

with open('04.txt', 'r') as file:
    data = file.read().split('\n\n')
''' Part 1 (r7check has to be removed from if)
r1 = re.compile(r'\bbyr:')
r2 = re.compile(r'\biyr:')
r3 = re.compile(r'\beyr:')
r4 = re.compile(r'\bhgt:')
r5 = re.compile(r'\bhcl:')
r6 = re.compile(r'\becl:')
r7 = re.compile(r'\bpid:')
'''
r1 = re.compile(r'\bbyr:(19[23456789]\d|200[012])')
r2 = re.compile(r'\biyr:20(1\d|20)')
r3 = re.compile(r'\beyr:20(2\d|30)')
r4 = re.compile(r'\bhgt:(1([5678]\d|9[0123])cm|(59|6\d|7[0123456])in)\b')
r5 = re.compile(r'\bhcl:#[0-9a-f]{6}')
r6 = re.compile(r'\becl:(amb|blu|brn|gry|grn|hzl|oth)\b')
r7 = re.compile(r'\bpid:(\d{9})')
r7check = re.compile(r'\bpid:(\d{10})')
valid = 0
for passport in data:
    if r1.search(passport) and r2.search(passport) and r3.search(passport) and r4.search(passport) and r5.search(passport) and r6.search(passport) and r7.search(passport) and not r7check.search(passport):
        #print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(r1.search(passport).group(0), r2.search(passport).group(0), r3.search(passport).group(0), r4.search(passport).group(0), r5.search(passport).group(0), r6.search(passport).group(0), r7.search(passport).group(0)))
        valid += 1
    else:
        pass  #print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(r1.search(passport), r2.search(passport), r3.search(passport), r4.search(passport), r5.search(passport), r6.search(passport), r7.search(passport)))
print(valid)
