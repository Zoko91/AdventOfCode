with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]

def parse_input(line):
    # For each line, parse the Id and the colors
    _, cards = line.split(':')
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

def how_many(deck):
    # How many lines i there is
    amount = 0
    for line in deck:
        amount += line[1]
    return amount

def get_amount(winning, deck):
    # Number of winning cards in deck
    score = 0
    for elem in deck:
        if elem in winning:
            score += 1
    return score

def get_line(doc, index):
    return doc[index]

total_sum = 0
for line in lines:
    # Part 1: return the score
    parsed_w, parsed_m = parse_input(line)
    total_sum += get_score(parsed_w,parsed_m)


i = 1
# [ [index of line, how many lines], [...] ]
how_many_lines = [[i, 1] for i in range(1, 199)]

for line in lines:
    # Part 2
    # Get the winning deck and in hand deck
    parsed_w, parsed_m = parse_input(line)

    # Get the amount of winning cards in deck
    # -- For each winning card, add one line to the deck
    amount_of_matching_numbers = get_amount(parsed_w, parsed_m)

    # Get the number of lines of the current i there is in the final computed deck
    quantity_of_lines = how_many_lines[i-1][1]

    # For j in n winning_card, the n following lines will get doubled
    for j in range(1,amount_of_matching_numbers+1,1):
        if (i+j-1) < 198:
            how_many_lines[i+j-1][1] += quantity_of_lines
    i += 1



# Part1: 21138
print(total_sum)

# Part2: 7185540
print(how_many(how_many_lines))

