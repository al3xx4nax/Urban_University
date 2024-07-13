def sum_three(*args):
    return sum(args)


def is_prime(func):
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        if results > 1:
            for i in range(2, (results // 2) + 1):
                if (results % i) == 0:
                    print("Составное")
                    break
                else:
                    print("Простое")
                    break
            else:
                print("Составное")
            return results

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
