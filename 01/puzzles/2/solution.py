f = open('input.txt')
data = f.read()
lines = data.splitlines()

cal_vals = []

def get_edge_digits(string):
    first_digit = None
    last_digit = None

    for (i, c) in enumerate(string):
        if (c.isdigit()):
            first_digit = (i, c)
            break

    last_digit = None
    for (i, c) in enumerate(string):
        if (c.isdigit()):
            if last_digit == None or i > last_digit[0]:
                last_digit = (i, c)

    return first_digit, last_digit

digit_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_edge_words(string):
    first_word = None
    last_word = None

    for word in digit_words:
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

def get_edges(string):
    first_digit, last_digit = get_edge_digits(string)    
    first_word, last_word = get_edge_words(string)

    first = None

    if first_digit == None:
        first = first_word[1]
    elif first_word == None:
        first = first_digit[1]
    else:
        first = first_digit[1] if first_digit[0] < first_word[0] else first_word[1]

    last = None

    if last_digit == None:
        last = last_word[1]
    elif last_word == None:
        last = last_digit[1]
    else:
        last = last_digit[1] if last_digit[0] > last_word[0] else last_word[1]
    
    if len(first) == 1:
        first = int(first)
    else:
        first = digit_words.index(first)

    if len(last) == 1:
        last = int(last)
    else:
        last = digit_words.index(last)

    return first, last

def get_cal_val(string):
    first, last = get_edges(string)
    cal_val = int(str(first) + str(last))
    return cal_val

for string in lines:
    cal_val = get_cal_val(string)
    cal_vals.append(cal_val)
    
answer = sum(cal_vals)
print('Answer: ', answer)