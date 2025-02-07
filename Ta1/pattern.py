def sum_of_digits(input_string):
    total = 0
    for char in input_string:
        if '0' <= char <= '9':
            total += int(char)
    return total

input_string = "123abc456"
digit_sum = sum_of_digits(input_string)
print(f"Sum of digits: {digit_sum} (Data type: {type(digit_sum)})")