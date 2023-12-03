f = open('input.txt')
data = f.read()
lines = data.splitlines()

cal_vals = []

for string in lines:
    first_digit = None
    last_digit = None
    for c in string:
        if (c.isdigit()):
            first_digit = c
            break
    for c in reversed(string):
        if (c.isdigit()):
            last_digit = c
            break
    cal_val = int(first_digit + last_digit)
    cal_vals.append(cal_val)

answer = sum(cal_vals)
print('Answer: ', answer)