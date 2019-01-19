# the key is a bubble and the value is the bubble it is inside
# topmost bubbles are not in this map

# example problem
bubble_chain = {
    'H': 'A',
    'A': 'E',
    'I': 'T',
}

# all off the bubbles
bubbles = set('HAEITSN')

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

winning_bubbles = []

for bubble in bubbles:
    popped = get_popped_bubbles(bubble, bubble_chain)
    if bubbly(bubbles - popped, bubble_chain, False):
        winning_bubbles.append(bubble)

print(winning_bubbles)
