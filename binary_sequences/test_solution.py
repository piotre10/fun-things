from main import easy_solution, fib_solution

test_cases = [
    [1, 1, '0'],
]


def test_easy_solution():
    for n, k, expected_result in test_cases:
        assert expected_result == easy_solution(n, k)


def test_fib_solution():
    for n, k, expected_result in test_cases:
        assert expected_result == fib_solution(n, k)
