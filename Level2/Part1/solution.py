import string


def solution(n, b):
    id_length = len(n)
    id_array = [n]
    cycled = False

    while not cycled:
        next_id = calculate_next_id(id_array[-1], id_length, b)

        if int(next_id) == 0:
            return 1

        cycle_length = get_cycle_length(next_id, id_array)
        if cycle_length:
            return cycle_length

        id_array.append(next_id)


def get_cycle_length(next_id, id_array):
    # return 1 if loop becomes stuck on a contstent
    if next_id == id_array[-1]:
        return 1
    # check if value has already appeared, indicating a loop
    if next_id in id_array[:-1]:
        return len(id_array) - id_array.index(next_id)
    return 0


def calculate_next_id(previous_id, id_length, base):
    x, y = get_x_and_y(previous_id, base)

    difference = calculate_difference(x, y, base)

    padded_difference = difference.zfill(id_length)

    return padded_difference


def calculate_difference(x, y, base):
    difference_base_10 = _calculate_difference_in_base_10(x, y, base)
    difference_base_n = _convert_base_10_int_to_base_n_string(
        difference_base_10, base)
    return difference_base_n


def get_x_and_y(previous_id, base):
    x_string, y_string = _get_x_and_y_strings(previous_id)
    x, y = _get_x_and_y_base_10(x_string, y_string, base)
    return x, y


def _get_x_and_y_base_10(x, y, base):
    return int(x, base), int(y, base)


def _get_x_and_y_strings(previous_id):
    digits = list(str(previous_id))
    sorted_digits = sorted(digits)

    y = ''.join(sorted_digits)
    x = y[::-1]

    return x, y


def _calculate_difference_in_base_10(x_base_10, y_base_10, base):
    return x_base_10 - y_base_10


def _convert_base_10_int_to_base_n_string(number, base):
    # Don't need to worry about negative numbers as
    # n is nonnegative
    # x will always be larger than y
    digs = string.digits

    if number == 0:
        return digs[0]

    digits = []

    while number:
        digits.append(
            digs[int(number % base)]
        )
        number = int(number / base)

    digits.reverse()
    return ''.join(digits)


if __name__ == '__main__':
    length = solution('210022', 3)
    print('length ------ ', length)
