from solution import product, solution


def test_solution():
    assert solution([2, 0, 2, 2, 0]) == "8"
    assert solution([-1, -3, 4, -5]) == "60"
    assert solution([-1, -3, 4, -5, 2]) == "120"
    assert solution([2, -3, 1, 0, -5]) == "30"
    str1 = "1235421415454545454545454544"
    str2 = "1714546546546545454544548544544545"
    prod = str(product([int(str1), int(str2)]))
    assert prod == "2118187521397235888154583183918321221520083884298838480662480"
    assert(solution([0, -1])) == "0"
    assert(solution([-1, -2])) == "2"
    assert(solution([1000] * 50)) == str(1000 ** 50)
    assert(solution([-1000] * 50)) == str(1000 ** 50)
    assert(solution([1000] * 49 + [-1000])) == str(1000 ** 49)
    assert solution([0]) == "0"
    assert solution([-1]) == "-1"


test_solution()