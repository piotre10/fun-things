from typing import Optional


def left_pad_with_zeros(s: str, n: int) -> str:
    """Pads string s to length n with 0s"""
    to_pad = max(n - len(s), 0)
    return to_pad * "0" + s


def sequence_is_legal(sequence: str) -> bool:
    """Checks if sequence is legal as described in task"""
    prev_is_one = False
    for character in sequence:
        if character == "0":
            prev_is_one = False
            continue

        if character == "1":
            if prev_is_one:
                return False

            prev_is_one = True

    return True


def generate_fib_numbers(n: int):
    """Generates first n fibonnaci numbers starting from 1,2"""
    if n == 1:
        return [1]

    res = [1, 2]
    for _ in range(n - 2):
        res.append(res[-1] + res[-2])

    return res


def zackendorf_encode_binary(n: int, fib_numbers: list[int]) -> Optional[str]:
    """Returns binary sequence representing zackendorf decomposition of number n
    using Fibonacci sequence fib_numbers if such decomposition cannot be achieved (n to large) returns None"""
    res = ""
    skip = False
    remainder = n

    if n == 0:
        return "0" * len(fib_numbers)

    for fib in reversed(fib_numbers):
        if skip:
            res += "0"
            skip = False
            continue

        if fib <= remainder:
            res += "1"
            remainder -= fib
            skip = True
            continue

        else:
            res += "0"

    if remainder != 0:
        return None

    return res


def easy_solution(N: int, K: int) -> str:
    legal_sequences_encountered = 0
    for i in range(2**N):
        sequence = f"{i :b}"
        if sequence_is_legal(sequence):
            legal_sequences_encountered += 1
            print(i, sequence)

        if legal_sequences_encountered >= K:
            return left_pad_with_zeros(sequence, N)

    return ""


def fib_solution(N: int, K: int) -> str:
    fib_numbers = generate_fib_numbers(N + 1)
    number_to_encode = K - 1
    if number_to_encode >= fib_numbers[-1]:
        return ""

    encoded = zackendorf_encode_binary(number_to_encode, fib_numbers[:-1])
    if encoded is None:
        print("Something went wrong")
        return ""
    return encoded
