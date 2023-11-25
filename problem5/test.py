from random import randint, seed
from solution import simpler_solution, solution


def test_solution_already_solved():
    assert solution(1, 1) == "0"


def test_solution_one_move():
    assert solution(2, 1) == "1"


def test_longer_solution():
    assert solution(4, 7) == "4"


def test_strings():
    assert solution("1", "1") == "0"


def test_0s():
    assert solution(0, 1) == "impossible"


def test_timeout():
    assert solution(0, 10 ** 50)


def test_impossible():
    assert solution(2, 4) == "impossible"


def test_negative_str():
    assert solution("-1", "1") == "impossible"


def test_large_numbers():
    seed(1337)
    for _ in range(10 ** 5):
        x, y = [randint(0, 10 ** 50)] * 2
        assert simpler_solution(x, y) == solution(x, y)
