def solution(start, length):
    result = 0
    for row_num in range(length):
        row_start = start + row_num * length
        row_length = length - row_num
        result ^= xor_from_n_for_length(row_start, row_length)

    return result


def xor_from_1_to_n(n):
    remainder = n & 0b11
    if remainder == 0:
        return n

    if remainder == 1:
        return 1

    if remainder == 2:
        return n + 1

    return 0


def xor_from_n_for_length(n, length):
    return xor_from_1_to_n(n + length - 1) ^ xor_from_1_to_n(n - 1)


def xor_row(start, length):
    if length <= 0:
        return 0

    return xor_from_n_for_length(start, start + length - 1)
