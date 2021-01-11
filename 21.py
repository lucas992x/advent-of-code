import re, copy

# Part 1
noallergens = []
possibs = {}
allingredients = []
with open('21.txt', 'r') as file:
    for line in file:
        ingredients, allergens = line.strip().split('(')
        ingredients = ingredients.strip().split(' ')
        allergens = re.sub(r'contains (.+)\)', r'\1', allergens).split(', ')
        for allergen in allergens:
            possib = possibs.get(allergen, None)
            if possib is None:
                possibs.update({allergen: ingredients})
            else:
                newpossib = [i for i in possib if i in ingredients]
                possibs.update({allergen: newpossib})
        for ingredient in ingredients:
            if ingredient not in noallergens:
                noallergens.append(ingredient)
        allingredients += ingredients

for allergen in possibs:
    for ingredient in possibs[allergen]:
        if ingredient in noallergens:
            noallergens.remove(ingredient)

counter = 0
for ingredient in noallergens:
    counter += allingredients.count(ingredient)

print(counter)

# Part 2
gridpossibs = []
withallergens = list(set([i for i in allingredients if i not in noallergens]))
for allergen in possibs:
    gridpossib = []
    for ingredient in withallergens:
        if ingredient in possibs[allergen]:
            gridpossib.append(1)
        else:
            gridpossib.append(0)
    gridpossibs.append(gridpossib)

while sum([sum(r) for r in gridpossibs]) > len(gridpossibs):
    for gridpossib in gridpossibs:
        if gridpossib.count(1) == 1:
            index = gridpossib.index(1)
            for gp in gridpossibs:
                if gp != gridpossib:
                    gp[index] = 0

allergens = list(possibs)
for j in range(len(allergens)):
    possibs.update({allergens[j]: withallergens[gridpossibs[j].index(1)]})

print(','.join([possibs[a] for a in sorted(possibs)]))
