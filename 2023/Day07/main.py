with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]

cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
all_camel_types = {'high card': 0,'one pair': 1,'two pair': 2,'three of a kind': 3,'full house': 4,'four of a kind': 5,'five of a kind': 6}

def get_rank(hand):
    hand_count = {}
    for letter in hand:
        hand_count[letter] = hand_count.get(letter, 0) + 1
    if len(hand_count) == 1:
        return all_camel_types["five of a kind"]
    elif len(hand_count) == 2:
        if 4 in hand_count.values() and 1 in hand_count.values():
            return all_camel_types["four of a kind"]
        else:
            return all_camel_types["full house"]
    elif len(hand_count) == 3:
        if 3 in hand_count.values():
            return all_camel_types["three of a kind"]
        else:
            return all_camel_types["two pair"]
    elif len(hand_count) == 4:
        return all_camel_types["one pair"]
    else:
        # High card
        return all_camel_types["high card"]

def parse_input(line):
    a, b = line.split(' ')
    # a = [letter for letter in a]
    return a, int(b)

def card_value(card, cards_dict):
    value = sum(cards_dict[letter] * 10 ** (8 - 2*i) for i, letter in enumerate(card))
    return value

def custom_sort_key(item):
    card, _ = parse_input(item)
    return card_value(card, cards)

list_to_hands = [[] for i in range(len(all_camel_types))]
# Loop to fill the list_to_hands
for line in lines:
    hand, bid = parse_input(line)
    list_to_hands[get_rank(hand)].append(line)

# Sort each list
list_to_hands_sorted = [sorted(list_to_order, key=custom_sort_key) for list_to_order in list_to_hands]
# How many elements ?
# print(sum([len(l) for l in list_to_hands_sorted]))

total_winnings = 0
current_rank = 1
for l in list_to_hands_sorted:
    for i in range(len(l)):
        _, bid = parse_input(l[i])
        total_winnings += bid * current_rank
        current_rank += 1

# Part1: 251120792 too low
print(total_winnings)
