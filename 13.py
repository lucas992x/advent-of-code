import math

''' Part 1
with open('13.txt', 'r') as file:
    data = file.read().splitlines()
earliest = int(data[0])
buses = [int(d) for d in data[1].split(',') if d != 'x']
mybus = 0
wait = max(buses)
for bus in buses:
    next = math.ceil(earliest / bus) * bus
    wt = next - earliest
    if wt < wait:
        wait = wt
        mybus = bus
print(wait * mybus)
'''
# code taken from github.com/KevinMichelle/Chinese-Remainder-Theorem
# small changes to make it work with Python 3
def egcd(a, b):
    auxiliar = (a, b)
    a = max(auxiliar)
    b = min(auxiliar)
    x = (1, 0)
    y = (0, 1)
    while a % b != 0:
        q = a // b
        c = a % b
        nx = x[0] - (x[1] * q)
        ny = y[0] - (y[1] * q)
        x = (x[1], nx)
        y = (y[1], ny)
        a = b
        b = c
    return (b, x[1], y[1])

def chinese(m, a):
    x = 0
    n = 1
    for i in m:
        n = n * i
    for i in range(0, len(m)):
        tmp = m[i]
        e = egcd(tmp, n // tmp)[1] * (n // tmp)
        x += e * a[i]
    while x <= 0:
        x = x + n
    return x

with open('13.txt', 'r') as file:
    data = file.read().splitlines()
buses = [int(d.replace('x', '0')) for d in data[1].split(',')]
realbuses = [b for b in buses if b > 0]
rests = [buses[j] - j for j in range(len(buses)) if buses[j] > 0]
sol = chinese(realbuses, rests)
print(sol)
