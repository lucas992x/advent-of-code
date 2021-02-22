orbits = {}
with open('06.txt', 'r') as file:
    for line in file:
        object1, object2 = line.strip().split(')')
        orbits.update({object2: object1})

# Part 1
countorbits = 0
for object in orbits:
    while orbits.get(object, None) is not None:
        countorbits += 1
        object = orbits[object]
print(countorbits)

# Part 2
myorbits = []
object = 'YOU'
while orbits.get(object, None) is not None:
    object = orbits[object]
    myorbits.append(object)

santaorbits = []
object = 'SAN'
while orbits.get(object, None) is not None:
    object = orbits[object]
    santaorbits.append(object)

node = [object for object in myorbits if object in santaorbits][0]
print(myorbits.index(node) + santaorbits.index(node))
