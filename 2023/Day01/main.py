with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]
numbers_dict = {'one': "1", 'two': "2", 'three': "3", 'four': "4", 'five': "5", 'six': "6", 'seven': "7", 'eight': "8", 'nine': "9"}
numbers_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total_cost = 0
j = 0
for line in lines:
    start = 0
    end = 0
    index_number = None
    # First index
    for i in range(len(line)):
        if line[i].isdigit():
            start = line[i]
            index_number = i
            break

    # Second index
    for i in range(len(line)-1,0,-1):
        if line[i].isdigit():
            end = line[i]
            break
        end = start

    # Used as verification
    # if j < 25:
    #     # print("i°", j+1, " Start: ", start, " End: ", end)

    cost = str(start)+str(end)
    total_cost += int(cost)
    j += 1

# Part one: 55447
print(total_cost)

def find_letter_number(word, order=True):
    test_word = ""
    i = 0
    if order:
        for l in word:
            test_word += l
            # Used as verification
            # print("i: ",i, " word: ",test_word)
            if l.isdigit():
                return l
            for subword in numbers_list:
                if subword in test_word:
                    return numbers_dict[subword]
            i += 1
    else:
        for l in word[::-1]:
            test_word += l
            # Used as verification
            # print("i: ", i, " word: ", test_word[::-1])
            if l.isdigit():
                return l
            for subword in numbers_list:
                if subword in test_word[::-1]:
                    return numbers_dict[subword]
            i += 1
    return None

total_cost = 0
for line in lines:
    # Get the first and second number adds them as string to build a 2 integers numbers then cast to it
    total_cost += int(find_letter_number(line)+find_letter_number(line,False))

# Part two:
print(total_cost)


