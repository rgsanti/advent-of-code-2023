f = open('input.txt')
DATA = f.read()
LINES = DATA.splitlines()

# print(LINES)

def get_history(string):
    values = [int(s) for s in string.split(' ')]
    return values

histories = []
for string in LINES:
    history = get_history(string)
    histories.append(history)

# print(histories)

def get_diff_sequence(sequence):
    diff_sequence = []
    for i in range(1, len(sequence)):
        diff_sequence.append(sequence[i] - sequence[i - 1])
    return diff_sequence

def get_diff_sequences(history):
    diff_sequences = []
    curr_sequence = history
    while True:
        next_diff_sequence = get_diff_sequence(curr_sequence)
        diff_sequences.append(next_diff_sequence)
        if not any(next_diff_sequence):
            break
        else:
            curr_sequence = next_diff_sequence
    return diff_sequences
    # sequence = []
    # for i in range(1, len(history)):
    #     sequence.append(history[i] - history[i - 1])
    # return sequence

history_diff_seqs_array = []
for index, history in enumerate(histories):
    diff_seqs = get_diff_sequences(history)
    history_diff_seqs_array.append(diff_seqs)

for index, history in enumerate(histories):
    history_diff_seqs_array[index].insert(0, history)

top_sequences = []

for history_diff_seqs in history_diff_seqs_array:
    # for i in range(len(history_diff_seqs) - 1, -1, -1):
    #     print(history_diff_seqs[i])
    seqs = history_diff_seqs[::-1]
    for index, seq in enumerate(seqs[1:]):
        # print(seq)
        # print(seqs[index][-1])

        # EXTRAPOLATE FORWARD
        # seq.append(seq[-1] + seqs[index][-1])

        # EXTRAPOLATE BACKWARD
        seq.insert(0, seq[0] - seqs[index][0])

    # print(seqs)
    top_sequences.append(seqs[-1])

print(top_sequences)

extrapolated_vals = []
for top_seq in top_sequences:
    extrapolated_vals.append(top_seq[0])

print(extrapolated_vals)
print(sum(extrapolated_vals))

# print(history_diff_seqs)

# print(histories)