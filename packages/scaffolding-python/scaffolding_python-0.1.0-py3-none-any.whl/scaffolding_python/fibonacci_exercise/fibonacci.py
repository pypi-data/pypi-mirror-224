def get_fibonacci_number(n: int) -> int:
    if (n <= 2):
        return n
    return get_fibonacci_number(n-1) + get_fibonacci_number(n-2)


def generate_fibonacci_series(long: int) -> list[int]:
    fibonacci_series: list[int] = []
    for n in range(long):
        fibonacci_series.append(
            get_fibonacci_number(n)
        )
    return fibonacci_series
