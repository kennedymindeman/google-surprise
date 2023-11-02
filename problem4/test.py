from solution import solution, xor_from_n_for_length


def test_xor_m_to_n() -> None:
    assert xor_from_n_for_length(0, 4) == 0
    assert xor_from_n_for_length(0, 5) == 4
    assert xor_from_n_for_length(17, 4) == 4


def test_solution() -> None:
    assert solution(0, 3) == 2
    assert solution(17, 4) == 14


test_xor_m_to_n()
test_solution()
