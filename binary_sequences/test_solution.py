from main import easy_solution, fib_solution

test_cases = [
    (1, 1, "0"),
    (1, 2, "1"),
    (5, 1, "00000"),
    (1, 3, ""),
    (20, 10, "00000000000000010001"),
    (7, 5, "0000101"),
    (9, 9, "000010000"),
]


def run_test_cases(func):
    for N, K, expected_res in test_cases:
        assert func(N, K) == expected_res


def test_easy_solution():
    run_test_cases(easy_solution)


def test_fib_solution():
    run_test_cases(fib_solution)
