with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]

cards_with_jokers = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}
all_camel_types = {'high card': 0,'one pair': 1,'two pair': 2,'three of a kind': 3,'full house': 4,'four of a kind': 5,'five of a kind': 6}

def get_rank(hand):
    hand_count = {}
    for letter in hand:
        hand_count[letter] = hand_count.get(letter, 0) + 1
    nb_joker = hand_count.get('J', 0)
    if len(hand_count) == 1:
        # AAAAA
        return all_camel_types["five of a kind"]
    elif len(hand_count) == 2:
        # AAAAJ or JJJJA
        if nb_joker == 1 or nb_joker == 4:
            return all_camel_types["five of a kind"]
        # AAAJJ or JJJAA
        elif 3 in hand_count.values() and (nb_joker == 2 or nb_joker == 3):
            return all_camel_types["five of a kind"]
        # AAAAQ
        elif 4 in hand_count.values() and 1 in hand_count.values():
            return all_camel_types["four of a kind"]
        # AAAQQ
        else:
            return all_camel_types["full house"]

    elif len(hand_count) == 3:
        # JJJBC
        if nb_joker == 3:
            return all_camel_types["four of a kind"]
        # AAABJ
        elif 3 in hand_count.values() and nb_joker == 1:
            return all_camel_types["four of a kind"]
        # AAQJJ
        elif nb_joker == 2 and (1 in hand_count.values()):
            return all_camel_types["four of a kind"]
        # AABBC
        else:
            # AABBJ
            if nb_joker == 1:
                return all_camel_types["full house"]
            # AAABC
            elif 3 in hand_count.values():
                return all_camel_types["three of a kind"]
            # AABBC
            else:
                return all_camel_types["two pair"]

    elif len(hand_count) == 4:
        # ABBCJ or AJJCD
        if nb_joker == 1 or nb_joker == 2:
            return all_camel_types["three of a kind"]
        # ABBCD
        else:
            return all_camel_types["one pair"]

    else:
        # ABCDJ
        if nb_joker == 1:
            return all_camel_types["one pair"]
        # ABCDE
        else:
            return all_camel_types["high card"]

def parse_input(line):
    a, b = line.split(' ')
    return a, int(b)

def card_value(card, cards_dict):
    value = sum(cards_dict[letter] * 10 ** (8 - 2*i) for i, letter in enumerate(card))
    return value

def custom_sort_key(item):
    card, _ = parse_input(item)
    return card_value(card, cards_with_jokers)

list_to_hands = [[] for i in range(len(all_camel_types))]
# Loop to fill the list_to_hands
for line in lines:
    hand, bid = parse_input(line)
    list_to_hands[get_rank(hand)].append(line)

# Sort each list
list_to_hands_sorted = [sorted(list_to_order, key=custom_sort_key) for list_to_order in list_to_hands]

total_winnings = 0
current_rank = 1
for l in list_to_hands_sorted:
    for i in range(len(l)):
        _, bid = parse_input(l[i])
        total_winnings += bid * current_rank
        current_rank += 1

# Part2: 251421071
print(total_winnings)
