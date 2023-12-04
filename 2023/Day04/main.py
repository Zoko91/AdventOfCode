with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]
lines2 = lines.copy

def parse_input(line):
    # For each line, parse the Id and the colors
    game_id, cards = line.split(':')
    w_card, m_card = cards.split('|')
    w_card = w_card[1:-1].split(' ')
    m_card = m_card[1:].split(' ')
    w_card = [item for item in w_card if item != '']
    m_card = [item for item in m_card if item != '']
    # print(w_card, m_card)
    return w_card, m_card

def get_score(winning, deck):
    score = -1
    for elem in deck:
        if elem in winning:
            score += 1
            # print("Winning number")
    if score == -1:
        return 0
    return 2**score


total_sum = 0
for line in lines:
    parsed_w, parsed_m = parse_input(line)
    total_sum += get_score(parsed_w,parsed_m)

# Part1: 21138
print(total_sum)

def augment_list(doc, index):
    print("")
