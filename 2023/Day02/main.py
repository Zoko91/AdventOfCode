with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]

def parse_input(line):
    # For each line, parse the Id and the colors
    game_id, colors = line.split(':')
    game_id = game_id.split(' ')[1]
    bags = colors.split(';')
    mini_green = 0
    mini_red = 0
    mini_blue = 0
    for bag in bags:
        bag = bag.split(',')
        for part in bag:
            part = part[1:]
            number, color = part.split(' ')
            if color == 'red':
                if int(number) > 12:
                    game_id =  0
                if int(number) > mini_red:
                    mini_red = int(number)
            elif color == 'blue':
                if int(number) > 14:
                    game_id = 0
                if int(number) > mini_blue:
                    mini_blue = int(number)
            elif color == 'green':
                if int(number) > 13:
                    game_id = 0
                if int(number) > mini_green:
                    mini_green = int(number)
    return int(game_id), mini_red, mini_blue, mini_green

possible_games_sum = 0
for line in lines:
    possible_games_sum += parse_input(line)[0]

power_games_sum = 0
for line in lines:
    red, blue, green = parse_input(line)[1:]
    power_games_sum += (red*blue*green)

# Part 1: 2377
print(possible_games_sum)

# Part 2: 71220
print(power_games_sum)
