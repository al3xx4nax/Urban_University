def test(a=25, b=False, c='Urban'):
    print(a, b, c)


test()


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(7))
