from solution import solution


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
