from utils import get_puzzle_input
TEXT, LINES = get_puzzle_input('input.txt')

# --- Part One ---

def get_first_digit(string):
    for char in string:
        if (char.isdigit()):
            return char

def get_last_digit(string):
    for char in reversed(string):
        if (char.isdigit()):
            return char

def calculate_cal_vals_one(lines):
    cal_vals = []

    for string in lines:
        first_digit = get_first_digit(string)
        last_digit = get_last_digit(string)
        cal_val = int(first_digit + last_digit)
        cal_vals.append(cal_val)
    
    return cal_vals

def part_one():
    cal_vals = calculate_cal_vals(LINES)
    answer = sum(cal_vals)
    print(f'Answer to Part One: {answer}')

# --- Part Two ---

DIGIT_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_first_digit_and_index(string):
    first_digit = None
    for (i, char) in enumerate(string):
        if (char.isdigit()):
            first_digit = (i, char)
            break
    return first_digit

def get_last_digit_and_index(string):
    last_digit = None
    for (i, char) in enumerate(string):
        if (char.isdigit()):
            if last_digit == None or i > last_digit[0]:
                last_digit = (i, char)
    return last_digit

def get_edge_digits(string):
    first_digit = get_first_digit_and_index(string)
    last_digit = get_last_digit_and_index(string)
    return first_digit, last_digit

def get_edge_words(string):
    first_word = None
    last_word = None

    for word in DIGIT_WORDS:
        if word in string:
            index = string.index(word)
            if first_word == None or index < first_word[0]:
                first_word = (index, word)

            occurrences = string.count(word)
            for _ in range(1, occurrences):
                index = string.index(word, index + 1)
            
            if last_word == None or index > last_word[0]:
                last_word = (index, word)

    return first_word, last_word

def resolve_first_edge(first_digit, first_word):
    if first_digit == None:
        first = first_word[1]
    elif first_word == None:
        first = first_digit[1]
    else:
        first = first_digit[1] if first_digit[0] < first_word[0] else first_word[1]

    return first

def resolve_last_edge(last_digit, last_word):
    if last_digit == None:
        last = last_word[1]
    elif last_word == None:
        last = last_digit[1]
    else:
        last = last_digit[1] if last_digit[0] > last_word[0] else last_word[1]

    return last

def convert_edge_to_int(edge):
    if len(edge) == 1:
        edge = int(edge)
    else:
        edge = DIGIT_WORDS.index(edge)

    return edge

def get_edge_values(string):
    first_digit, last_digit = get_edge_digits(string)    
    first_word, last_word = get_edge_words(string)

    first_edge = resolve_first_edge(first_digit, first_word)
    last_edge = resolve_last_edge(last_digit, last_word)

    first = convert_edge_to_int(first_edge)
    last = convert_edge_to_int(last_edge)

    return first, last

def calculate_cal_vals_two(lines):
    cal_vals = []

    for string in lines:
        first, last = get_edge_values(string)
        cal_val = int(first + last)
        cal_vals.append(cal_val)
    
    return cal_vals

def part_two():
    cal_vals = calculate_cal_vals(LINES)
    answer = sum(cal_vals)
    print(f'Answer to Part Two: {answer}')

# --- Execute Solutions ---

part_one()
part_two()