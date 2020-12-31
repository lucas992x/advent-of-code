import re

# compute a single operation
def CalcOper(expr):
    search = r'(\d+) ([\+\*]) (\d+)'
    num1 = re.sub(search, r'\1', expr)
    oper = re.sub(search, r'\2', expr)
    num2 = re.sub(search, r'\3', expr)
    if oper == '+':
        res = int(num1) + int(num2)
    else:
        res = int(num1) * int(num2)
    return str(res)

# compute an expression without parentheses
def CalcPar(expr):
    ''' Part 1
    while re.search(r'[\+\*]', expr):
        search = r'^(\d+) ([\+\*]) (\d+) (.+)$'
        if re.search(search, expr):
            expr = re.sub(search, r'{} \4'.format(CalcOper(re.sub(search, r'\1 \2 \3', expr))), expr)
        else:
            expr = CalcOper(expr)
    '''
    while '+' in expr:
        search = r'^(.* )?(\d+ \+ \d+)( .*)?$'
        subexpr = re.sub(search, r'\2', expr)
        expr = re.sub(r'\b{}\b'.format(subexpr.replace('+', '\\+')), CalcOper(subexpr), expr)
    while '*' in expr:
        search = r'^(.* )?(\d+ \* \d+)( .*)?$'
        subexpr = re.sub(search, r'\2', expr)
        expr = re.sub(r'\b{}\b'.format(subexpr.replace('*', '\\*')), CalcOper(subexpr), expr)
    return expr

# compute entire expression
def CalcExpr(expr):
    while '(' in expr:
        search = r'^.*\(([^\(\)]+)\).*$'
        subexpr = re.sub(search, r'\1', expr)
        res = CalcPar(subexpr)
        expr = expr.replace('({})'.format(subexpr), res)
    res = CalcPar(expr)
    if re.search(r'^\d+$', res):
        return int(res)
    else:
        print(res)

with open('18.txt', 'r') as file:
    exprs = file.read().splitlines()

tot = 0
for expr in exprs:
    tot += CalcExpr(expr)
print(tot)
# 1157545085054808240 (too high)
# 119224703357054 (too high)
