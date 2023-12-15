with open('input.txt') as inpt:
    data = inpt.read().strip()

sequences = [sequence for sequence in data.split(',')]

def seq_to_val(sequence):
    val = 0
    for char_ in sequence:
        ascii_ = ord(char_)
        val += ascii_
        val *= 17
        val %= 256
    return val

total = 0
for sequence in sequences:
    total += seq_to_val(sequence)

print(total)
