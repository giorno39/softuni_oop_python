from functools import wraps


def multiply(num):
    def decorator(func):
        @wraps(func)
        def wrapper(n):
            result = func(n) * num
            return result

        return wrapper

    return decorator


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))

