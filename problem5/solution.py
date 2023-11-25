def solution(x, y):
    steps = 0
    x = int(x)
    y = int(y)

    while True:
        if x < 1 or y < 1:
            return "impossible"

        if x == 1 or y == 1:
            return str(steps + max([x, y]) - 1)

        if x < y:
            quotient = y // x
            steps += quotient
            y -= x * quotient
        else:
            quotient = x // y
            steps += quotient
            x -= y * quotient


def simpler_solution(x, y):
    steps = 0
    x = int(x)
    y = int(y)

    while True:
        if x < 1 or y < 1:
            return "impossible"

        if x == 1 and y == 1:
            return steps

        if x < y:
            y -= x
        else:
            x -= y

        steps += 1
