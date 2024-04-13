def test(*params):
    print(params)


test(33, 'Urban', False, 55)


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(7))
