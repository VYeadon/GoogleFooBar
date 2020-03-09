import string
digs = string.digits + string.ascii_letters


def solution(n, b):
    length_of_id = len(n)
    id_array = [n]
    cycled = False
    while not cycled:
        new_id = calculate_new_id(id_array[-1], length_of_id, b)
        print(new_id)
        if int(new_id) is 0:
            return 1

        cycle_length = check_cycle_length(n, new_id, id_array)
        if cycle_length:
            return cycle_length

        id_array.append(new_id)


def check_cycle_length(original_id, new_id, id_array):
    if new_id == id_array[-1]:
        return 1
    if new_id in id_array[:-1]:
        return len(id_array) - id_array.index(new_id)
    return 0


def calculate_new_id(previous_id, length_of_id, base):
    x, y = _get_x_and_y(previous_id)
    difference = calculate_difference(x, y, base)
    padded_difference = difference.zfill(length_of_id)
    return padded_difference


def calculate_difference(x, y, base):
    x_base_10 = int(x, base)
    y_base_10 = int(y, base)
    difference = x_base_10 - y_base_10
    difference_base_n = convert_base_10_int_to_base(difference, base)
    return difference_base_n


def _get_x_and_y(previous_id):
    digits = list(str(previous_id))
    sorted_digits = sorted(digits)
    y = ''.join(sorted_digits)
    x = y[::-1]
    return x, y


# function to convert number n from base 10 to base b
def convert_base_10_int_to_base(number, base):
    if number < 0:
        sign = -1
    elif number == 0:
        return digs[0]
    else:
        sign = 1

    number *= sign
    digits = []

    while number:
        digits.append(digs[int(number % base)])
        number = int(number / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)


if __name__ == '__main__':
    length = solution('1211', 10)
    print('length ------ ', length)
