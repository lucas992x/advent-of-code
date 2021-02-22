def SingleTransform(value, subnum):
    return (value * subnum) % 20201227

def FullTransform(lsize, subnum):
    value = 1
    for j in range(lsize):
        value = SingleTransform(value, subnum)
    return value

def FindLoopSize(pubkey):
    value = 1
    subnum = 7
    lsize = 0
    while value != pubkey:
        value = SingleTransform(value, subnum)
        lsize += 1
    return lsize

#pubkey = [5764801, 17807724]  # example
pubkey = [12578151, 5051300]  # my puzzle input

clsize = FindLoopSize(pubkey[0])
enckey = FullTransform(clsize, pubkey[1])
''' Alternative
dlsize = FindLoopSize(pubkey[1])
enckey = FullTransform(dlsize, pubkey[0])
'''
print(enckey)
