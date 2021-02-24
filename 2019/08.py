with open('08.txt', 'r') as file:
    data = file.read().strip()

width = 25
height = 6
area = width * height
layers = []
while data != '':
    layers.append(data[:area])
    data = data[area:]

# Part 1
zeros = [layer.count('0') for layer in layers]
layerindex = zeros.index(min(zeros))
ones = layers[layerindex].count('1')
twos = layers[layerindex].count('2')
print(ones * twos)

# Part 2
message = ''
for i in range(len(layers[0])):
    j = 0
    while layers[j][i] == '2':
        j += 1
    message += layers[j][i]

for j in range(height):
    print(message[:width].replace('0', ' '))
    message = message[width:]
