def primes():
    """Бесконечный генератор простых чисел"""

    yield 2
    i = 3
    while True:
        if all(i % div for div in range(2, int(i ** 0.5) + 1)):
            yield i
        i += 2
        