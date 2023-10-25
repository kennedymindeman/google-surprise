def solution(xs):
    if len(xs) == 1:
        return str(xs[0])

    negatives = [x for x in xs if x < 0]
    positives = [x for x in xs if x > 0]
    if len(negatives) % 2 != 0:
        negatives.remove(max(negatives))

    filtered_numbers = positives + negatives
    if filtered_numbers == []:
        return "0"

    return str(product(filtered_numbers))


def product(numbers):
    if numbers == []:
        raise ValueError("Product of empty iterable is undefined!")

    prod = 1
    for number in numbers:
        prod *= number

    return prod
