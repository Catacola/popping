#bubble_chain = {
#    'H': ['HA', 'HAE'],
#    'HA': ['HAE'],
#    'HAE': [],
#    'I': ['IT'],
#    'IT': [],
#    'S': [],
#    'N': [],
#  }

bubble_chain = {
    'H': 'A',
    'A': 'E',
    'I': 'T',
}

bubbles = set('HAEITSN')

state = {}

def bubbly(bubbles, bubble_chain, my_turn):

    if len(bubbles) == 1 and my_turn:
        return True

    bottom_bubbles = get_bottom_bubbles(bubbles, bubble_chain)

    #for bubble in bottom_bubbles:


    return bottom_bubbles

def get_bottom_bubbles(bubbles, bubble_chain):
    in_deg = {bubble: 0 for bubble in bubbles}
    for outer_bubble in bubble_chain.values():
        in_deg[outer_bubble] += 1

    return [bubble for bubble, deg in in_deg.items() if deg == 0]

print(bubbly(bubbles, bubble_chain, True))
