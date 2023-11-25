def solution(x, y):
    steps = 0
    x = int(x)
    y = int(y)
    while x != 1 or y != 1:
        if x < 1 or y < 1:
            return "impossible"

        if x < y:
            y -= x
        else:
            x -= y

        steps += 1

    return str(steps)
