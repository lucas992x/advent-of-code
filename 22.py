import re, copy

with open('22.txt', 'r') as file:
    data = [re.sub(r'Player \d+:\n', '', d) for d in file.read().split('\n\n')]
decks = []
for d in data:
    decks.append([int(n) for n in d.strip().split('\n')])

def AdjustDecks(winner, loser):
    winner.append(winner[0])
    winner.append(loser[0])
    winner.remove(winner[0])
    loser.remove(loser[0])
    return winner, loser

def PlayGame(deck1, deck2):
    history = []
    winner = None
    while winner is None:
        if [deck1, deck2] in history:
            winner = [deck1, '1']
        else:
            history.append([copy.deepcopy(deck1), copy.deepcopy(deck2)])
            if len(deck1) > deck1[0] and len(deck2) > deck2[0]:
                index1 = deck1[0] + 1
                index2 = deck2[0] + 1
                subwinner = PlayGame(deck1[1:index1], deck2[1:index2])[1]
                if subwinner == '1':
                    deck1, deck2 = AdjustDecks(deck1, deck2)
                else:
                    deck2, deck1 = AdjustDecks(deck2, deck1)
            else:
                if deck1[0] > deck2[0]:
                    deck1, deck2 = AdjustDecks(deck1, deck2)
                else:
                    deck2, deck1 = AdjustDecks(deck2, deck1)
            if len(deck1) == 0:
                winner = [deck2, '2']
            elif len(deck2) == 0:
                winner = [deck1, '1']
    return winner

''' Part 1
def PlayRound(deck1, deck2):
    if deck1[0] > deck2[0]:
        deck1, deck2 = AdjustDecks(deck1, deck2)
    else:
        deck2, deck1 = AdjustDecks(deck2, deck1)
    return deck1, deck2

winner = []
while winner == []:
    decks = PlayRound(*decks)
    if len(decks[0]) == 0:
        winner = decks[1]
    elif len(decks[1]) == 0:
        winner = decks[0]
'''
winner = PlayGame(*decks)[0]
score = 0
for j in range(1, len(winner) + 1):
    score += j * winner[-j]
print(score)
