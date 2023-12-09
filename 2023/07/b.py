with open ('input.txt') as f:
    lines = f.read().splitlines()

replace = {
    'T': 'A',
    'J': 'B',
    'Q': 'C',
    'K': 'D',
    'A': 'E',
}

def replace_card(card, use_wildcard = False):
    if use_wildcard and card == 'J':
        return '1'

    if card in replace.keys():
        return replace[card]
    return card

def get_hand_type(hand, use_wildcard = False):
    hist = {}
    for card in hand:
        hist.setdefault(card, 0)
        hist[card] += 1

    wildcard_key = replace['J']
    wildcard_count = 0
    if use_wildcard and wildcard_key in hist:
        wildcard_count = hist[wildcard_key]
        del hist[wildcard_key]

    m = max(hist.values(), default=0) + wildcard_count
    l = len(hist.values())

    if m == 5:
        return str(6) # 5 of a kind
    if m == 4:
        return str(5) # 4 of a kind
    elif m == 3 and l == 2:
        return str(4) # full house
    elif m == 3: # 
        return str(3) # 3 of a kind
    elif m == 2 and l == 3:
        return str(2) # two pairs
    elif m == 2:
        return str(1) # one pair
    else:
        return str(0) # high card

def calc_hash(hand):
    hex_code_wildcard = ''
    hex_code = ''
    for card in hand:
        hex_code_wildcard += replace_card(card, True)
        hex_code += replace_card(card, False)

    hand_type = get_hand_type(hex_code, True)
    hex_code = hand_type + hex_code_wildcard
    return int(hex_code, 16)

hands = []
for line in lines:
    hand, bid = line.split(' ')
    bid = int(bid)

    hash = calc_hash(hand)
    hands.append((hash, bid))

hands.sort()

sum = 0
for index in range(0, len(hands)):
    hash, bid = hands[index]
    rank = index + 1
    sum += rank * bid

print(sum)

