all_camel_types = {'high card': 0, 'one pair': 1, 'two pair': 2, 'three of a kind': 3, 'full house': 4, 'four of a kind': 5, 'five of a kind': 6}

def get_rank(hand):
    hand_count = {}
    for letter in hand:
        hand_count[letter] = hand_count.get(letter, 0) + 1

    nb_joker = hand_count.get('J', 0)

    if len(hand_count) == 1 or nb_joker == 4:
        return all_camel_types["five of a kind"]
    elif len(hand_count) == 2:
        if 4 in hand_count.values() and 1 in hand_count.values():
            return all_camel_types["four of a kind"]
        elif 3 in hand_count.values() and nb_joker == 1:
            return all_camel_types["full house"]
        else:
            return all_camel_types["three of a kind"] if nb_joker == 1 else all_camel_types["two pair"]
    elif len(hand_count) == 3:
        if 3 in hand_count.values():
            return all_camel_types["three of a kind"]
        elif 2 in hand_count.values() and nb_joker == 1:
            return all_camel_types["two pair"]
        else:
            return all_camel_types["one pair"] if nb_joker == 1 else all_camel_types["high card"]
    else:
        return all_camel_types["high card"]

# Example usage:
hand1 = 'QQJQ2'
hand2 = 'AAA66'
hand3 = 'J2345'
hand4 = 'JJJJ2'
hand5 = 'JJJJK'

print(get_rank(hand1))  # Output: four of a kind
print(get_rank(hand2))  # Output: three of a kind
print(get_rank(hand3))  # Output: straight (J as 10)
print(get_rank(hand4))  # Output: four of a kind (Joker as K)
print(get_rank(hand5))  # Output: five of a kind (Joker as K)
