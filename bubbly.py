# bubble_chain
# the key is a bubble and the value is the bubble it is inside
# topmost bubbles are not in this map
#
# bubbles: all of the bubbles

# example problem
sample_chain = {
    'H': 'A',
    'A': 'E',
    'I': 'T',
}

sample_bubbles = set('HAEITSN')

# problem 1
chain1 = {
    'A': 'R',
    'R': 'C',
    'G': 'C',
    'H': 'C',
    'S': 'H',
    'U': 'S',
    'I': 'U',
    'T': 'S',
    'V': 'S',
    'E': 'V',
    'L': 'E',
}

#bubbles1 = set('NARCGHSUITVEL')
bubbles1 = set()
for k, v in chain1.items():
    bubbles1.add(k)
    bubbles1.add(v)
bubbles1.add('N')

#problem 2
chain2 = {
    'G': 'E',
    'V': 'H',
    'P': 'V',
    'R': 'P',
    'F': 'I',
    'S': 'F',
    'N': 'F',
    'U': 'N',
    'T': 'I',
    'C': 'T',
    'A': 'C',
    'L': 'A',
}

#bubbles2 = set('GEVPRHFSUNITALC')
bubbles2 = set()
for k, v in chain2.items():
    bubbles2.add(k)
    bubbles2.add(v)

#problem 3
chain3 = {
    'P': 'F',
    'L': 'F',
    'U': 'L',
    'H': 'F',
    'R': 'H',
    'E': 'H',
    'A': 'E',
    'N': 'A',
    'Y': 'A',
    'M': 'Y',
    'C': 'E',
    'V': 'C',
    'I': 'C',
    'G': 'I',
    'T': 'I',
    'S': 'T',
}

#bubbles3 = set('FLUPHREMYNACVGITS')
bubbles3 = set()
for k, v in chain3.items():
    bubbles3.add(k)
    bubbles3.add(v)

# problem 4
chain4 = {
    'V': 'A',
    'S': 'A',
    'P': 'S',
    'E': 'P',
    'Y': 'I',
    'N': 'Y',
    'F': 'N',
    'U': 'Y',
    'T': 'U',
    'H': 'T',
    'G': 'B',
    'R': 'M',
    'K': 'R',
    'C': 'R',
    'L': 'C',
}

bubbles4 = set()
for k, v in chain4.items():
    bubbles4.add(k)
    bubbles4.add(v)

# problem 5
chain5 = {
    'N': 'F',
    'Z': 'N',
    'K': 'N',
    'P': 'K',
    'L': 'F',
    'G': 'L',
    'M': 'G',
    'S': 'L',
    'Y': 'S',
    'I': 'S',
    'C': 'I',
    'V': 'I',
    'H': 'V',
    'E': 'L',
    'B': 'E',
    'A': 'E',
    'R': 'A',
    'D': 'E',
    'T': 'D',
    'U': 'T',
}

bubbles5 = set()
for k, v in chain5.items():
    bubbles5.add(k)
    bubbles5.add(v)

# problem 6
chain6 = {
    'W': 'S',
    'I': 'C',
    'R': 'C',
    'P': 'R',
    'D': 'A',
    'U': 'A',
    'X': 'U',
    'T': 'A',
    'F': 'T',
    'G': 'F',
    'B': 'A',
    'H': 'B',
    'L': 'B',
    'N': 'L',
    'E': 'B',
    'Y': 'E',
    'Z': 'E',
    'V': 'Z',
    'M': 'Z',
    'K': 'M',
}

bubbles6 = set()
for k, v in chain6.items():
    bubbles6.add(k)
    bubbles6.add(v)

# problem 7
chain7 = {
    'E': 'N',
    'H': 'P',
    'W': 'H',
    'Q': 'F',
    'B': 'Q',
    'V': 'B',
    'I': 'V',
    'G': 'R',
    'U': 'G',
    'L': 'U',
    'Z': 'L',
    'C': 'Z',
    'Y': 'T',
    'A': 'Y',
    'J': 'Y',
    'M': 'J',
    'S': 'T',
    'D': 'S',
    'K': 'D',
    'X': 'K',
}

bubbles7 = set()
for k, v in chain7.items():
    bubbles7.add(k)
    bubbles7.add(v)

state = {}

def bubbly(bubbles, bubble_chain, my_turn):

    # print('Bubbly called with bubbles: ', bubbles, ', my_turn: ', my_turn)

    state_key = get_state_key(bubbles, my_turn)

    if state_key in state:
        return state[state_key]

    if len(bubbles) == 1:
        state[state_key] = my_turn
        return my_turn

    if len(bubbles) == 0:
        state[state_key] = not my_turn
        return not my_turn

    if my_turn:
        for bubble in bubbles:
            popped = get_popped_bubbles(bubble, bubble_chain)

            if bubbly(bubbles - popped, bubble_chain, not my_turn):
                state[state_key] = True
                return True

        state[state_key] = False
        return False

    else:
        for bubble in bubbles:
            popped = get_popped_bubbles(bubble, bubble_chain)

            if not bubbly(bubbles - popped, bubble_chain, not my_turn):
                state[state_key] = False
                return False

        state[state_key] = True
        return True


def get_popped_bubbles(bubble, bubble_chain):
    popped = set(bubble)
    parent = bubble_chain.get(bubble, None)
    while parent is not None:
        popped.add(parent)
        parent = bubble_chain.get(parent, None)
    return popped


def get_state_key(bubbles, my_turn):
    return (''.join(sorted(bubbles)), my_turn)

def winning_moves(bubbles, bubble_chain):
    global state
    state = {}

    winning_bubbles = []

    for bubble in bubbles:
        popped = get_popped_bubbles(bubble, bubble_chain)
        if bubbly(bubbles - popped, bubble_chain, False):
            winning_bubbles.append(bubble)

    return winning_bubbles

print('Sample problem:')
print(winning_moves(sample_bubbles, sample_chain))
print()

print('Problem 1:')
print(winning_moves(bubbles1, chain1))
print()

print('Problem 2:')
print(winning_moves(bubbles2, chain2))
print()

print('Problem 3:')
print(winning_moves(bubbles3, chain3))
print()

print('Problem 4:')
print(winning_moves(bubbles4, chain4))
print()

print('Problem 5:')
print(winning_moves(bubbles5, chain5))
print()

print('Problem 6:')
print(winning_moves(bubbles6, chain6))
print()

print('Problem 7:')
print(winning_moves(bubbles7, chain7))
print()

