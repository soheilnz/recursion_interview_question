def sumOf(n):
    assert 0 <= n == int(n), "invalid value"
    if n == 0:
        return 0
    return int(n % 10) + sumOf(n//10)


# print(sumOf(44456))
# print(sumOf(-11))
# print(sumOf(123.5))
